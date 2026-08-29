---
id: ef861772-9ac2-4816-abfe-d61631dcb6c6
identifier: PET-35
type: Task
title: Показывать ошибки сохранения и удаления события
state: Done
priority: medium
labels: [calendar, frontend]
parent: PET-70
pages:
  - PET/pages/calendar/dobavlenie-sobytiya-frontend.md
  - PET/pages/calendar/redaktirovanie-sobytiya-frontend.md
  - PET/pages/calendar/udalenie-sobytiya-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: handleSubmitForm при добавлении события и обработчик удаления вызывают мутацию и сразу переходят/закрывают экран без ожидания результата — при ошибке сервера (сеть, 400, 404, 500) пользователь не узнаёт об этом, событие визуально пропадает без реального сохранения/удаления.
Что сделать: дожидаться результата мутации перед навигацией; при ошибке показывать snackbar/alert и не покидать экран (для добавления) или восстанавливать карточку в списке (для удаления).
Затронутые файлы: src/pages/add-event/add-event-controller.tsx, компонент со свайпом удаления события (см. event-card.tsx).
