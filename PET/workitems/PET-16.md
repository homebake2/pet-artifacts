---
id: fd85a09d-6d5c-4af9-97ab-a2840c872fab
identifier: PET-16
type: Task
title: Вынести JWT-секрет из исходного кода
state: Done
priority: medium
labels: [auth, backend]
parent: PET-68
pages:
  - PET/pages/auth/vhod-i-registratsiya-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: секрет подписи токенов захардкожен в utils/jwt.go (var jwtKey = []byte("ваш_секретный_ключ")), не читается из окружения/конфигурации.
Риск: любой, у кого есть доступ к репозиторию, может подделывать токены любых пользователей.
Решение: читать секрет из переменной окружения JWT_SECRET при старте сервиса; при отсутствии переменной — запускаться с дефолтным значением "ваш_секретный_ключ".
Затронутые файлы: utils/jwt.go, main.go, docker-compose.yml, docs/deploy.md.
