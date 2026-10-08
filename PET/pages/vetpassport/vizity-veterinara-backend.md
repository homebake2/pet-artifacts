---
id: 03ce7186-1f41-4a73-8ec1-c8821f096790
title: Посещения ветеринара — Backend
parent_page: PET/pages/vetpassport/index.md
created_at: 2026-09-09
updated_at: 2026-10-06
---
## Смотрите также

* [Требования: Ветпаспорт](index.md)

* [Общие требования: Формат ошибок API](../common/obschie-trebovaniya-format-oshibok-api.md)

* [Общие требования: IDOR и владение ресурсами](../common/obschie-trebovaniya-idor-i-vladenie-resursami.md)

* [Общие требования: Soft-delete](../common/obschie-trebovaniya-soft-delete.md)

* [Общие требования: Файлы сущностей](../integrations/obschie-trebovaniya-fayly-sushchnostei.md) — подключение `owner_type = vet_visit_file`.

## Назначение

Флоу ведёт список посещений ветеринара в разделе «Медкарта»: дата посещения, причина визита, клиника/врач, заметка, до 10 прикреплённых файлов. Не создаёт и не связывается с событиями календаря.

## Модель данных

```
CREATE TABLE vet_visit (
  id           uuid PRIMARY KEY,
  pet_id       uuid NOT NULL REFERENCES pet(id),
  visit_date   date NOT NULL,
  reason       text NOT NULL,   -- ≤ 200 символов
  clinic       text NULL,       -- ≤ 200 символов
  note         text NULL,       -- ≤ 1000 символов
  idempotency_key text NULL,    -- Idempotency-Key запроса создания; уникален на пару (pet_id, idempotency_key) среди строк с ключом
  deleted_at   timestamptz NULL,
  created_at   timestamptz NOT NULL DEFAULT now(),
  updated_at   timestamptz NOT NULL DEFAULT now()
);
```

## Действующие лица и предусловия

Те же, что у «Вакцинации — Backend».

## Основной сценарий

**Список.** `GET /pet/{id}/vet-visits` — неудалённые визиты питомца, отсортированные по `visit_date` убыв. Элемент — `VetVisitResponse`: `id`, `visit_date`, `reason`, `clinic`, `note`, `files_count`.

**Создание.** `POST /pet/{id}/vet-visits`. Тело: `visit_date` (обязательно, `YYYY-MM-DD`), `reason` (обязательно, ≤200), `clinic` (опционально, ≤200), `note` (опционально, ≤1000). Опциональный заголовок `Idempotency-Key` (UUID v4, иначе `400`): ключ хранится в строке записи и уникален на пару `(pet_id, idempotency_key)`; повторный запрос с тем же ключом для того же питомца не создаёт новую запись, а возвращает `201 Created` с `id` ранее созданной — в том числе при одновременных запросах с одним ключом и когда созданная запись уже мягко удалена (удаление не освобождает ключ). `201 Created` с телом `{id}` — идентификатором созданного визита.

**Редактирование.** `PATCH /vet-visits/{id}` — частичное обновление любого из `visit_date`, `reason`, `clinic`, `note`. `204 No Content`.

**Удаление.** `DELETE /vet-visits/{id}` — мягкое удаление. `204 No Content`; повторный вызов — `404` («уже удалено»).

## Бизнес-правила и валидация

* Обязательные поля создания: `visit_date`, `reason`.

* `visit_date` не ограничен диапазоном — допускает как прошлые (задокументированные постфактум), так и будущие (запланированные) визиты.

* Питомец должен принадлежать инициатору и не быть мягко удалён — иначе `404`/`400`.

## Обработка ошибок

| Статус | Условие |
| --- | --- |
| 400 | Не заполнено обязательное поле / `visit_date` не `YYYY-MM-DD` / `reason`/`clinic` длиннее 200 / `note` длиннее 1000 / `Idempotency-Key` не UUID v4 |
| 401 | Токен отсутствует или недействителен |
| 404 | Питомец/визит не найдены, мягко удалены или принадлежат другому пользователю |
| 500 | Внутренняя ошибка БД |

## Хранение состояния и побочные эффекты

Изменяет только таблицу `vet_visit`. Не затрагивает данные питомца, не создаёт события.
