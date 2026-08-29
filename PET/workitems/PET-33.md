---
id: 3beb4ea8-8113-4ddb-a0e3-0661313f2bf6
identifier: PET-33
type: Task
title: Реализовать редактирование события в интерфейсе (главная задача)
state: Done
priority: medium
labels: [calendar, frontend]
parent: PET-70
pages:
  - PET/pages/calendar/redaktirovanie-sobytiya-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: API полностью готово и покрыто тестами на бэкенде, клиентские заготовки уже есть (useGetEvent, usePutEvent, маппер mapEvent, расширенная zod-схема с id), но нет ни экрана, ни точки входа (тап по карточке события ничего не делает — onPress не задан), ни маршрута в навигаторе.
Решение (принято): переиспользовать AddEventPage/AddEventForm в режиме редактирования (наиболее вероятный замысел, судя по расположению mapEvent в add-event/mappers): добавить обработчик onPress на EventCard, передавать eventId через навигацию, предзагружать данные события через useGetEvent, вызывать мутацию обновления при сохранении. Обработать офлайн-режим отдельно (см. п.4 задачи «добавление события», если применимо к редактированию).
Важно: PUT /events/{id} переименовывается в PATCH /events/{id} в рамках tasks/calendar-backend.md, п.6 — реализовывать эту задачу сразу под новый метод (usePatchEvent вместо usePutEvent), не переиспользуя старое имя хука, так как отдельного релиза под PUT-версию не запланировано.
Затронутые файлы: src/shared/ui/molecules/pet-events/pet-events.tsx (или где рендерится EventCard), src/entities/events/ui/event-card/event-card.tsx, src/pages/add-event/add-event.tsx, add-event-controller.tsx, src/app/navigation/navigators/calendar-stack-navigator.tsx, src/entities/calendar/api/use-put-event.ts (переименовать/заменить на PATCH-версию).
