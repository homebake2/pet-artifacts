---
id: c40bf4d7-7933-4ce8-8c0f-2a1848dcb272
identifier: PET-56
type: Task
title: PUT на несуществующий профиль должен возвращать ошибку, а не тихий 200
state: Done
priority: medium
labels: [profile, backend]
parent: PET-71
pages:
  - PET/pages/profile/redaktirovanie-profilya-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: если у пользователя ещё нет строки в profile, PUT /profile не создаёт её и не сообщает об этом — SQL UPDATE не находит строк, но сервер всё равно отвечает 200 OK, будто обновление прошло успешно.
Что сделать: после UPDATE проверять количество затронутых строк (RowsAffected); если 0 — возвращать 404 с понятным сообщением («профиль не найден, используйте POST для создания») вместо 200.
Затронутые файлы: handlers/profile.go.
