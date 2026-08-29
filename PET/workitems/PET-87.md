---
id: 3ef3bc18-12d5-4e71-98e5-f306ad94d560
identifier: PET-87
type: Task
title: Добавить поле type в ответ GET /events/{id}
state: Done
priority: medium
labels: [calendar, backend]
created_at: 2026-08-27
updated_at: 2026-08-27
---
**Проблема:** схема `GetEventIdResponseRequest` (используется и для `201` ответа `POST /events`, и для `200` ответа `GET /events/{id}`) не содержит поле `type` (тип события: weight/urine/defecation/vomit/diarrhea/other), хотя оно есть в `GetEventResponse` (используется в `/activities` и `/pet/{id}/events`).

**Как обнаружено:** при реализации редактирования события на клиенте (PET-33, экран AddEventPage в режиме edit) для сетевого режима данных используется `GET /events/{id}` для предзагрузки формы. Без `type` в ответе клиент не может предзаполнить тип события — сейчас поле остаётся пустым, и пользователю приходится выбирать тип заново при каждом редактировании события в network-режиме (см. `src/entities/calendar/hooks/use-get-event-by-id.ts`, комментарий про ограничение спеки).

**Что сделать:** добавить `type` (enum `GetEventEnum`) как обязательное поле в схему `GetEventIdResponseRequest` в `openapi/reference/api.yaml` и в реализации бэкенда для `GET /events/{id}` (и заодно для `POST /events`-ответа, раз схема общая). После обновления спеки прогнать `npm run codegen` на фронтенде и убрать временный workaround (`type: undefined`) в `use-get-event-by-id.ts`.

**Затронутые файлы (backend):** `openapi/reference/api.yaml` (схема `GetEventIdResponseRequest`), обработчик `GET /events/{id}`.

**Затронутые файлы (frontend, после обновления спеки):** `src/entities/calendar/hooks/use-get-event-by-id.ts`.
