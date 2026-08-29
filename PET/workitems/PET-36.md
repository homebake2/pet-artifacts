---
id: 52f3bbd7-ff6b-4af8-9a95-112209e8963f
identifier: PET-36
type: Task
title: Унифицировать обязательность поля value
state: Done
priority: medium
labels: [calendar, frontend]
parent: PET-70
pages:
  - PET/pages/calendar/dobavlenie-sobytiya-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: на клиенте поле value не обязательно, на сервере — обязательно (400, если не передано). Форма может позволить отправить запрос, который сервер отклонит.
Что сделать: сделать value обязательным в клиентской схеме валидации формы добавления/редактирования события, синхронно с серверным требованием.
Затронутые файлы: src/entities/calendar/schemas.ts, src/pages/add-event/form/add-event-form/add-event-form.tsx.
