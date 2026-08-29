---
id: 30c9b059-b28d-45c4-bbc3-d550201584d6
identifier: PET-27
type: Task
title: Вернуть 404 для чужого/несуществующего питомца в GET /activities
state: Done
priority: medium
labels: [calendar, backend]
parent: PET-70
pages:
  - PET/pages/calendar/prosmotr-kalendarya-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: /activities — единственный из четырёх событийных эндпоинтов, где обращение к чужому или несуществующему pet_id не даёт 404, а тихо возвращает 200 с {"pet_name": "", "items": []}. Клиент не может отличить «у питомца правда нет событий» от «питомца не существует/не мой».
Что сделать: привести поведение к остальным эндпоинтам событий — возвращать 404, если питомец не найден или не принадлежит профилю из токена.
Затронутые файлы: handlers/events.go (GetActivitiesHandler).
