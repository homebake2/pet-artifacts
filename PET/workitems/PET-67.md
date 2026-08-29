---
id: dd307477-296a-4b95-8781-7ca13c45c902
identifier: PET-67
type: Task
title: Отобразить login на экране просмотра профиля
state: Done
priority: medium
labels: [profile, frontend]
parent: PET-71
pages:
  - PET/pages/profile/prosmotr-profilya-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: поля id и login, которые бэкенд присылает в GET /profile, нигде не используются и не отображаются на экране.
Решение (принято): отобразить login на экране просмотра профиля как неизменяемое поле (пользователь логинится этим значением, логично его показать). Поле id (равно user_id, см. profile-backend.md, п.5) действительно не нужно UI — не выводить его в маппер вовсе.
Затронутые файлы: src/pages/profile/mappers/map-user-profile.ts, src/pages/profile/profile.tsx.
