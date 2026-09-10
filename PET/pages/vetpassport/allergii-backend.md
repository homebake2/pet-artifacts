---
id: fd04d02d-471b-4fe7-b9a5-c70fb885f847
title: Аллергии — Backend
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

* [Общие требования: Файлы сущностей](../integrations/obschie-trebovaniya-fayly-sushchnostei.md) — подключение `owner_type = allergy_file`.

* [Справочник значений (словари enum)](../common/spravochnik-znachenii-slovari-enum.md), раздел «Ветпаспорт — Степень тяжести аллергии».

## Назначение

Флоу ведёт список аллергий питомца: аллерген, реакция, дата выявления, степень тяжести, заметка, до 10 прикреплённых файлов.

## Модель данных

```
CREATE TABLE allergy (
  id             uuid PRIMARY KEY,
  pet_id         uuid NOT NULL REFERENCES pet(id),
  allergen       text NOT NULL,   -- ≤ 100 символов
  reaction       text NULL,       -- ≤ 200 символов
  detected_date  date NULL,
  severity       text NOT NULL,   -- 'mild' | 'moderate' | 'severe', см. справочник
  note           text NULL,       -- ≤ 1000 символов
  deleted_at     timestamptz NULL,
  created_at     timestamptz NOT NULL DEFAULT now(),
  updated_at     timestamptz NOT NULL DEFAULT now()
);
```

## Действующие лица и предусловия

Те же, что у «Вакцинации — Backend».

## Основной сценарий

**Список.** `GET /pet/{id}/allergies` — неудалённые аллергии питомца, отсортированные по `created_at` убыв. Элемент — `AllergyResponse`: `id`, `allergen`, `reaction`, `detected_date`, `severity`, `note`, `files_count`.

**Создание.** `POST /pet/{id}/allergies`. Тело: `allergen` (обязательно, ≤100), `reaction` (опционально, ≤200), `detected_date` (опционально, `YYYY-MM-DD`), `severity` (обязательно, `mild`/`moderate`/`severe`), `note` (опционально, ≤1000). Опциональный `Idempotency-Key`. `201 Created` с `AllergyDetailResponse` (все поля + `files`).

**Редактирование.** `PATCH /allergies/{id}` — частичное обновление любого из `allergen`, `reaction`, `detected_date`, `severity`, `note`. `204 No Content`.

**Удаление.** `DELETE /allergies/{id}` — мягкое удаление. `204 No Content`; повторный вызов — `404` («уже удалено»).

## Бизнес-правила и валидация

* Обязательные поля создания: `allergen`, `severity`. `reaction` и `detected_date` — опциональны (диагноз аллергии не всегда сопровождается точной датой выявления).

* `severity` строго ограничен значениями справочника (`mild`, `moderate`, `severe`).

* Питомец должен принадлежать инициатору и не быть мягко удалён — иначе `404`/`400`.

## Обработка ошибок

| Статус | Условие |
| --- | --- |
| 400 | Не заполнено обязательное поле / `detected_date` не `YYYY-MM-DD` / `severity` не из справочника / `allergen` длиннее 100 / `reaction` длиннее 200 / `note` длиннее 1000 |
| 401 | Токен отсутствует или недействителен |
| 404 | Питомец/аллергия не найдены, мягко удалены или принадлежат другому пользователю |
| 500 | Внутренняя ошибка БД |

## Хранение состояния и побочные эффекты

Изменяет только таблицу `allergy`. Не затрагивает данные питомца, не создаёт события.
