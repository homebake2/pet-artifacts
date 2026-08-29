---
id: 0d3c4814-bafb-4506-b85e-40ba4db813ed
identifier: PET-30
type: Task
title: Ввести лимиты на notes/value и диапазон from..to
state: Done
priority: medium
labels: [calendar, backend]
parent: PET-70
pages:
  - PET/pages/calendar/dobavlenie-sobytiya-backend.md
  - PET/pages/calendar/prosmotr-kalendarya-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: нет ограничения на длину notes/value (потенциально неограниченные строки) и нет ограничения на максимальный диапазон from..to в /activities (можно запросить диапазон в несколько лет).
Решение (принято): notes и value — максимум 500 символов каждое; диапазон from..to в /activities — не более 366 дней. При превышении возвращать 400 VALIDATION_ERROR с понятным сообщением («Диапазон дат не должен превышать 366 дней» / «Поле notes/value не должно превышать 500 символов»).
Затронутые файлы: handlers/events.go, models/pet.go (структуры событий).
