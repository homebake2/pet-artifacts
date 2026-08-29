---
id: f364fdde-75b3-4d80-8857-bb0b9e88d23f
identifier: PET-32
type: Task
title: Переименовать PUT /events/{id} в PATCH
state: Done
priority: medium
labels: [calendar, backend]
parent: PET-70
pages:
  - PET/pages/calendar/redaktirovanie-sobytiya-backend.md
  - PET/pages/calendar/redaktirovanie-sobytiya-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: метод называется PUT, но фактически не требует передачи всех полей и не заменяет ресурс полностью (частичное обновление по переданным полям) — вводит в заблуждение относительно стандартной семантики PUT.
Решение (принято): переименовать в PATCH /events/{id} — это breaking change, требует синхронного изменения на обеих сторонах в одном релизе:
backend: заменить регистрацию маршрута в main.go (mux.HandleFunc("/events/", ...) — метод проверяется внутри EventIDResonseHandler, заменить проверку r.Method == http.MethodPut на http.MethodPatch), обновить open-api/spec.json.
frontend: перегенерировать кодоген (orval) под новый метод в event-controller.ts, обновить usePutEvent/переименовать в usePatchEvent при реализации задачи «редактирование события» (см. tasks/calendar-frontend.md, п.1 — редактирование события ещё не реализовано на UI, поэтому это удобный момент для смены метода без ущерба существующим пользователям).
Затронутые файлы: handlers/events.go, main.go, open-api/spec.json, src/shared/api/codegen/api/event-controller.ts, src/entities/calendar/api/use-put-event.ts.
