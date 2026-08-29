---
id: e23ddb71-9dc2-42b9-a23a-5d547a9f22eb
identifier: PET-25
type: Task
title: Различать типы ошибок при логине
state: Done
priority: medium
labels: [auth, frontend]
parent: PET-68
pages:
  - PET/pages/auth/vhod-i-registratsiya-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: все ошибки, кроме 403, показывают один и тот же текст «Логин или пароль неверные» — включая 500 и сетевые сбои, что вводит в заблуждение.
Что сделать: различать 400 VALIDATION_ERROR (показывать ошибку валидации полей), 403 (текущий текст про неверный пароль) и прочие/сетевые ошибки (общее сообщение «сервис недоступен, попробуйте позже»).
Затронутые файлы: src/pages/auth/auth-connector.tsx, src/pages/auth/form/auth-form/auth-form.tsx.
