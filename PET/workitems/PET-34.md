---
id: 97821225-0702-4e3a-b3ba-36ec883a3d76
identifier: PET-34
type: Task
title: Инвалидировать кэш активностей после добавления, редактирования и удаления события
state: Done
priority: medium
labels: [calendar, frontend]
parent: PET-70
pages:
  - PET/pages/calendar/dobavlenie-sobytiya-frontend.md
  - PET/pages/calendar/prosmotr-kalendarya-frontend.md
  - PET/pages/calendar/redaktirovanie-sobytiya-frontend.md
  - PET/pages/calendar/udalenie-sobytiya-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: ни в useDeleteEvent, ни в API-хуках создания/обновления нет вызовов invalidateQueries для ключа ['activities', petId, ...] — список календаря может не обновиться сразу после возврата с экрана добавления/удаления события.
Что сделать: добавить инвалидацию соответствующего ключа React Query в onSuccess мутаций создания, обновления и удаления события.
Затронутые файлы: src/entities/calendar/hooks/use-add-event.ts, use-delete-event.ts (сущность), src/entities/calendar/api/use-post-event.ts, use-put-event.ts, use-delete-event.ts (api), src/entities/calendar/api/queries.ts.
