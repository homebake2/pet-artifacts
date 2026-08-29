---
id: cfc00b1e-f327-4c22-a3ae-9db46c9e5514
identifier: PET-20
type: Task
title: Добавить эндпоинт удаления аккаунта
state: Done
priority: medium
labels: [auth, backend]
parent: PET-68
created_at: 2026-08-24
updated_at: 2026-08-24
---
Проблема: пункт «Удалить аккаунт» на фронтенде сейчас ничего не делает — соответствующего backend-эндпоинта нет ни в open-api/spec.json, ни в handlers/.
Решение (принято): добавить DELETE /profile (или отдельный DELETE /account — выбрать по консистентности с остальным API), требующий авторизации. Хендлер удаляет строку из users по id из токена; каскадное удаление profile, pet, event уже обеспечено внешними ключами ON DELETE CASCADE (см. database/migrations/000001_init_schema.up.sql), дополнительная ручная очистка не нужна. Ответ — 204 No Content. Добавить путь в OpenAPI и роутинг в main.go.
Затронутые файлы: handlers/ (новый хендлер или расширение profile.go), main.go, open-api/spec.json.
