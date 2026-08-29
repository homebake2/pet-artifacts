---
id: 12b8d07b-84d8-4fec-a0c3-b4d4358a38cf
identifier: PET-59
type: Task
title: Задокументировать смысл поля id в ответе GET /profile
state: Done
priority: medium
labels: [profile, backend]
parent: PET-71
pages:
  - PET/pages/profile/prosmotr-profilya-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: поле id в ответе фактически равно user_id, а не первичному ключу таблицы profile (который никогда не возвращается клиенту).
Решение (принято): поле не переименовывать (не ломать существующий контракт без явной необходимости) — явно задокументировать в OpenAPI и в коде (комментарий у ProfileResponse.ID), что это идентификатор пользователя (users.id), а не собственный id строки profile.
Затронутые файлы: models/profile.go, open-api/spec.json.
