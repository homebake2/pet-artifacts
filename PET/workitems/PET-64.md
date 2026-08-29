---
id: 4ba035dd-ed5a-4883-aa1e-309ee39558f6
identifier: PET-64
type: Task
title: Инвалидировать кэш профиля после сохранения
state: Done
priority: medium
labels: [profile, frontend]
parent: PET-71
pages:
  - PET/pages/profile/prosmotr-profilya-frontend.md
  - PET/pages/profile/redaktirovanie-profilya-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: после успешного PUT/POST кэш GET /profile не инвалидируется — экран просмотра профиля может показать не только что введённые данные, а прежние значения из кэша.
Что сделать: вызывать invalidateQueries/refetch для ключа профиля в onSuccess мутации редактирования.
Затронутые файлы: src/entities/profile/api/queries.ts, use-put-profile.ts, use-post-profile.ts.
