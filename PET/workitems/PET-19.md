---
id: 8b2a1625-5744-4915-a332-5d8a42d41f1f
identifier: PET-19
type: Task
title: Добавить минимальную серверную валидацию пароля
state: Done
priority: medium
labels: [auth, backend]
parent: PET-68
pages:
  - PET/pages/auth/vhod-i-registratsiya-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: password принимается как произвольная строка без ограничения длины/сложности на сервере — валидация полностью отдана фронтенду.
Решение (принято): минимальная длина пароля — 8 символов, без требований к сложности (цифры/спецсимволы не обязательны). Добавить проверку в authenticateOrRegister, возвращающую 400 VALIDATION_ERROR с сообщением «Пароль должен быть не короче 8 символов» при нарушении.
Затронутые файлы: handlers/auth.go.
