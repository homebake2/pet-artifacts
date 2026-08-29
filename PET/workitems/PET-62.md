---
id: 6921587f-e2db-4268-af6f-0296ea22a732
identifier: PET-62
type: Task
title: Использовать POST при первом заполнении профиля
state: Done
priority: medium
labels: [profile, frontend]
parent: PET-71
pages:
  - PET/pages/profile/redaktirovanie-profilya-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: экран редактирования всегда вызывает PUT, независимо от того, существует ли профиль на сервере. Метод usePostProfile нигде не задействован. После фикса backend-задачи «PUT на несуществующий профиль» (см. profile-backend.md, п.2) первое сохранение через PUT начнёт возвращать 404.
Что сделать: определять на экране, есть ли у пользователя профиль (например, по результату GET /profile — пустой/404 vs заполненный), и вызывать POST при первом заполнении, PUT — при последующих правках.
Затронутые файлы: src/pages/profile-edit/profile-edit-connector.tsx, src/entities/profile/api/use-post-profile.ts, src/entities/profile/api/use-put-profile.ts.
