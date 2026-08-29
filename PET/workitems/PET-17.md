---
id: 2163ee20-14b3-49d2-89e4-ef19e9ac5071
identifier: PET-17
type: Task
title: Сделать ошибку сохранения refresh_token фатальной везде
state: Done
priority: medium
labels: [auth, backend]
parent: PET-68
pages:
  - PET/pages/auth/obnovlenie-tokena-backend.md
  - PET/pages/auth/vhod-i-registratsiya-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: при логине/авто-регистрации (handlers/auth.go: authenticateOrRegister) ошибка UPDATE users SET refresh_token=... только логируется, клиент получает 200 OK с токенами, которые сервер не смог сохранить. При POST /auth/refresh та же ошибка фатальна (500).
Решение (принято): сделать ошибку фатальной в обоих местах — при неудачном сохранении refresh_token в authenticateOrRegister возвращать 500 INTERNAL_ERROR и не отдавать клиенту токены, аналогично RefreshTokenHandler. Клиент никогда не должен получать токены, которые сервер не смог сохранить.
Затронутые файлы: handlers/auth.go (authenticateOrRegister).
