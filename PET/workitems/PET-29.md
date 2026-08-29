---
id: da691783-2efe-4eb2-b4a2-a28cef6c3f3f
identifier: PET-29
type: Task
title: Явно валидировать формат date при создании события
state: Done
priority: medium
labels: [calendar, backend]
parent: PET-70
pages:
  - PET/pages/calendar/dobavlenie-sobytiya-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: в UpdateEventHandler формат date явно проверяется (time.Parse(time.RFC3339, ...) → 400 при ошибке), а в CreateEventHandler аналогичной явной проверки не найдено — неясно, приводит ли некорректный формат к 500 от БД или к тихому сохранению некорректного значения.
Что сделать: добавить в CreateEventHandler такую же явную проверку формата date (RFC3339) с возвратом 400 VALIDATION_ERROR при ошибке, симметрично обновлению.
Затронутые файлы: handlers/events.go (CreateEventHandler).
