---
id: ad286bb1-4056-4b0c-8f00-01300c09f4d1
identifier: PET-26
type: Task
title: Убрать неиспользуемый postRegister
state: Done
priority: medium
labels: [auth, frontend]
parent: PET-68
pages:
  - PET/pages/auth/vhod-i-registratsiya-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: оба пути /auth/login и /auth/register работают на бэкенде одинаково, но фронтенд использует только postLogin; postRegister из кодогенерации нигде не вызывается.
Решение (принято): удалить неиспользуемый postRegister/связанные хуки из кодовой базы фронтенда — держать единственную точку входа postLogin, поведение бэкенда для обоих путей идентично, различать их на клиенте незачем.
Затронутые файлы: src/shared/api/codegen/api/auth-controller.ts, src/entities/auth/api/*.
