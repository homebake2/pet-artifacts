---
id: ee859f36-e19a-4525-aace-dd19d1162e71
title: Заболевания — Backend
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

* [Общие требования: Файлы сущностей](../integrations/obschie-trebovaniya-fayly-sushchnostei.md) — подключение `owner_type = disease_file`.

* [Справочник значений (словари enum)](../common/spravochnik-znachenii-slovari-enum.md), раздел «Ветпаспорт — Статус заболевания».

## Назначение

Флоу ведёт список заболеваний питомца в разделе «Медкарта»: название, дата постановки диагноза, статус (активно/вылечено), заметка, до 10 прикреплённых файлов. Заболевание не создаёт и не связывается с событиями календаря.

## Модель данных

```
CREATE TABLE disease (
  id               uuid PRIMARY KEY,
  pet_id           uuid NOT NULL REFERENCES pet(id),
  name             text NOT NULL,     -- ≤ 100 символов
  diagnosed_date   date NOT NULL,
  status           text NOT NULL,     -- 'active' | 'cured', см. справочник
  note             text NULL,         -- ≤ 1000 символов
  deleted_at       timestamptz NULL,
  created_at       timestamptz NOT NULL DEFAULT now(),
  updated_at       timestamptz NOT NULL DEFAULT now()
);
```

## Действующие лица и предусловия

Те же, что у «Вакцинации — Backend»: авторизованный владелец питомца; питомец существует, принадлежит инициатору, не мягко удалён.

## Основной сценарий

**Список.** `GET /pet/{id}/diseases` — неудалённые заболевания питомца, отсортированные по `diagnosed_date` убыв. Элемент — `DiseaseResponse`: `id`, `name`, `diagnosed_date`, `status`, `note`, `files_count`.

**Создание.** `POST /pet/{id}/diseases`. Тело: `name` (обязательно, ≤100), `diagnosed_date` (обязательно, `YYYY-MM-DD`), `status` (обязательно, `active`/`cured`), `note` (опционально, ≤1000). Опциональный `Idempotency-Key` — тот же механизм, что у событий/вакцинаций. Возвращает `201 Created` с `DiseaseDetailResponse` (все поля + `files`).

**Редактирование.** `PATCH /diseases/{id}` — частичное обновление любого из `name`, `diagnosed_date`, `status`, `note`. `204 No Content`.

**Удаление.** `DELETE /diseases/{id}` — мягкое удаление (`deleted_at`). `204 No Content`; повторный вызов — `404`, трактуется как «уже удалено».

## Бизнес-правила и валидация

* Обязательные поля создания: `name`, `diagnosed_date`, `status`.

* `status` строго ограничен значениями справочника (`active`, `cured`) — см. [Справочник значений (словари enum)](../common/spravochnik-znachenii-slovari-enum.md); значение по умолчанию на форме — `active`, но backend не подставляет значение по умолчанию сам — поле обязательно в запросе.

* `note` — свободный комментарий, не более 1000 символов.

* Питомец должен принадлежать инициатору и не быть мягко удалён — иначе `404`/`400` (см. «Общие требования: IDOR и владение ресурсами»).

## Обработка ошибок

| Статус | Условие |
| --- | --- |
| 400 | Не заполнено обязательное поле / `diagnosed_date` не `YYYY-MM-DD` / `status` не из справочника / `name` длиннее 100 / `note` длиннее 1000 |
| 401 | Токен отсутствует или недействителен |
| 404 | Питомец/заболевание не найдены, мягко удалены или принадлежат другому пользователю |
| 500 | Внутренняя ошибка БД |

## Хранение состояния и побочные эффекты

Изменяет только таблицу `disease`. Не создаёт и не изменяет события, не затрагивает данные питомца.
