---
id: e85f7fd7-d641-49f8-9170-9ff422251a66
title: Вакцинации — Backend
parent_page: PET/pages/vetpassport/index.md
workitems: []
created_at: 2026-09-09
updated_at: 2026-09-09
---
## Смотрите также

* [Требования: Ветпаспорт](index.md)

* [Общие требования: Формат ошибок API](../common/obschie-trebovaniya-format-oshibok-api.md)

* [Общие требования: IDOR и владение ресурсами](../common/obschie-trebovaniya-idor-i-vladenie-resursami.md)

* [Общие требования: Soft-delete](../common/obschie-trebovaniya-soft-delete.md)

* [Общие требования: Файлы сущностей](../integrations/obschie-trebovaniya-fayly-sushchnostei.md) — подключение `owner_type = vaccination_file`.

* [Справочник значений (словари enum)](../common/spravochnik-znachenii-slovari-enum.md), раздел «Ветпаспорт — Статус вакцинации (computed)».

* [Модель значения события и реестр метрик](../common/model-znacheniya-sobytiya-i-metriki.md) — тип события `other`, используемый для напоминаний, создаваемых этим флоу.

## Назначение

Флоу ведёт список вакцинаций питомца: название, дата введения, дата следующей вакцинации, опционально — два связанных напоминания в календаре (на дату введения и/или на дату следующей вакцинации) и до 10 прикреплённых файлов.

## Модель данных

```
CREATE TABLE vaccination (
  id                 uuid PRIMARY KEY,
  pet_id             uuid NOT NULL REFERENCES pet(id),
  name               text NOT NULL,       -- ≤ 100 символов
  administered_date  date NOT NULL,
  next_date          date NULL,
  administered_event_id  uuid NULL,       -- event.id напоминания на administered_date, если создано
  next_event_id          uuid NULL,       -- event.id напоминания на next_date, если создано
  deleted_at         timestamptz NULL,
  created_at         timestamptz NOT NULL DEFAULT now(),
  updated_at         timestamptz NOT NULL DEFAULT now()
);
```

## Действующие лица и предусловия

* Инициатор — авторизованный владелец питомца.

* Питомец должен существовать, принадлежать инициатору и не быть мягко удалённым.

## Основной сценарий

**Список.** `GET /pet/{id}/vaccinations` — возвращает неудалённые вакцинации питомца, отсортированные по `next_date` (сначала записи с ближайшей `next_date`, затем записи без `next_date` — по `administered_date` убыв.). Каждый элемент — `VaccinationResponse`: `id`, `name`, `administered_date`, `next_date`, `has_events` (boolean — `administered_event_id IS NOT NULL OR next_event_id IS NOT NULL`), `files_count` (см. «Общие требования: Файлы сущностей», по аналогии с `event.files_count`). Проверка владения — по `pet_id`, см. «Бизнес-правила».

**Создание.** `POST /pet/{id}/vaccinations`. Тело: `name` (обязательно, ≤100), `administered_date` (обязательно, `YYYY-MM-DD`), `next_date` (опционально, `YYYY-MM-DD`), `add_event_on_administered` (boolean, по умолчанию `false`), `add_event_on_next` (boolean, по умолчанию `false`, требует непустого `next_date`), `event_time` (`HH:mm`, обязательно, если хотя бы один из двух флагов выше — `true`). Опциональный заголовок `Idempotency-Key` (тот же механизм, что у `POST /events`, привязка по `(pet_id, idempotency_key)`).

1. Система проверяет владение питомцем (см. «Бизнес-правила»).
2. Система валидирует поля тела (см. «Бизнес-правила»).
3. Система вставляет строку `vaccination`.
4. Если `add_event_on_administered` — создаёт событие `type=other`, `value.label = "Вакцинация: " + name` (обрезка до 50 символов лимита `other.label`, см. «Модель значения события и реестр метрик»), `date = administered_date` + `event_time`, `notes = null`, привязанное к тому же питомцу; сохраняет его `id` в `administered_event_id`.
5. Аналогично для `add_event_on_next` и `next_event_id`, с `date = next_date` + `event_time`.
6. Возвращает `201 Created` с `VaccinationDetailResponse` (все поля строки + `files`, см. «Общие требования: Файлы сущностей»).

**Редактирование.** `PATCH /vaccinations/{id}`. Тело — частичное, любое из: `name`, `administered_date`, `next_date`, `add_event_on_administered`, `add_event_on_next`, `event_time`.

* Если `add_event_on_administered` меняется с `false`/отсутствует на `true` (или ранее `administered_event_id IS NULL`) — создаётся новое событие-напоминание, как в шаге 4 создания (`event_time` берётся из запроса либо из уже сохранённого значения, если в этом запросе не передан, — как минимум один раз `event_time` должен быть определён, иначе 400).
* Если `add_event_on_administered` меняется на `false`, а `administered_event_id` не `NULL` — связанное событие мягко удаляется (обычным механизмом soft-delete события, см. «Удаление события — Backend»), `administered_event_id` очищается.
* Если `administered_date` меняется, а `administered_event_id` не `NULL` — система обновляет `date` связанного события тем же значением (пересоздание не требуется: связь «один флаг — одно событие» не подвержена риску массового размножения строк, в отличие от лекарств, см. «Лекарства — Backend»).
* Симметрично — для `add_event_on_next`/`next_event_id`/`next_date`.
* Прочие поля (`name`) обновляются как переданы, без побочных эффектов на события.

**Удаление.** `DELETE /vaccinations/{id}` — мягко удаляет запись (`deleted_at`) и, если есть, мягко удаляет `administered_event_id`/`next_event_id`. `204 No Content`. Повторный вызов — `404`, трактуется клиентом как «уже удалено» (см. «Общие требования: Soft-delete»).

## Бизнес-правила и валидация

* Обязательные поля создания: `name`, `administered_date`. `next_date` — опционально.

* `next_date` не проверяется на «позже `administered_date`» — сервер допускает любые сочетания дат (переиспользование одной и той же формы для внесения задним числом уже выполненных курсов).

* `event_time` обязателен, если создаётся хотя бы одно напоминание (`add_event_on_administered` или `add_event_on_next` — `true`); в противном случае напоминания не создаются, `event_time` игнорируется, если передан.

* `add_event_on_next = true` без `next_date` — `400`.

* Питомец должен принадлежать инициатору и не быть мягко удалён — иначе `404`/`400` соответственно, по общей политике (см. [Общие требования: IDOR и владение ресурсами](../common/obschie-trebovaniya-idor-i-vladenie-resursami.md)).

* **Статус («Просрочена» / «Скоро» / «Актуальна») не хранится и не возвращается backend'ом** — вычисляется на клиенте из `next_date` (см. «Вакцинации — Frontend»). Backend возвращает только сырые даты.

## Обработка ошибок

| Статус | Условие |
| --- | --- |
| 400 | Не заполнено обязательное поле / дата не `YYYY-MM-DD` / `event_time` не `HH:mm` / нужен `event_time`, но не передан ни разу / `add_event_on_next=true` без `next_date` / `name` длиннее 100 символов |
| 401 | Токен отсутствует или недействителен |
| 404 | Питомец/вакцинация не найдены, мягко удалены или принадлежат другому пользователю |
| 500 | Внутренняя ошибка БД |

## Хранение состояния и побочные эффекты

Создание/редактирование/удаление вакцинации может дополнительно создавать/обновлять/мягко удалять до двух строк `event` (см. «Основной сценарий»). Данные питомца не затрагиваются.
