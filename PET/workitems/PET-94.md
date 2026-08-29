---
id: f1e3735a-70b9-49be-a00d-7afc480c34c6
identifier: PET-94
type: Task
title: Поднять минимальную длину пароля на клиенте до 8 символов
state: Backlog
priority: medium
labels: [auth, frontend]
parent: PET-88
pages:
  - PET/pages/auth/vhod-i-registratsiya-frontend.md
created_at: 2026-08-27
updated_at: 2026-08-30
---
Клиентская Zod-схема сейчас требует пароль от 6 символов, бэкенд — от 8. Нужно поднять минимум на клиенте до 8, чтобы валидация совпадала с сервером и пользователь не мог отправить пароль, который бэкенд всё равно отклонит.
