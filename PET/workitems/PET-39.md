---
id: c690b3fe-2c9f-452d-9ecc-b492af3d1911
identifier: PET-39
type: Task
title: Унифицировать способ получения активностей питомца
state: Done
priority: medium
labels: [calendar, frontend]
parent: PET-70
pages:
  - PET/pages/calendar/prosmotr-kalendarya-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: в кодовой базе два независимых способа получить данные /activities с разными ключами кэша React Query: queries.activities.list (используется на календаре) и отдельный useGetEventsByPetId с фиксированным диапазоном «год назад — год вперёд» и ключом ['activities', petId, 'pet-detail'] (используется на карточке питомца).
Что сделать: унифицировать через единую фабрику ключей queries.activities.list, убрать дублирующий independent-ключ, чтобы инвалидация кэша (см. задачу №2) затрагивала оба места использования одновременно.
Затронутые файлы: src/entities/calendar/hooks/use-get-events-by-pet-id.ts, src/entities/calendar/api/queries.ts.
