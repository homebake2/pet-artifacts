---
id: c84a7281-bb29-4988-a794-977b5d708558
identifier: PET-37
type: Task
title: Добавить индикатор загрузки при сохранении события
state: Done
priority: medium
labels: [calendar, frontend]
parent: PET-70
pages:
  - PET/pages/calendar/dobavlenie-sobytiya-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: кнопка «Сохранить» не блокируется на время выполнения postEventMutate — нет визуального индикатора «сохранение…».
Что сделать: дизейблить кнопку и показывать индикатор загрузки на время выполнения мутации.
Затронутые файлы: src/pages/add-event/form/add-event-form/add-event-form.tsx.
