---
id: db8479ea-884d-43fb-aa82-879ae44bb6c6
identifier: PET-55
type: Task
title: Устранить гонку в POST /profile
state: Done
priority: medium
labels: [profile, backend]
parent: PET-71
pages:
  - PET/pages/profile/redaktirovanie-profilya-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: проверка count == 0 и последующий INSERT выполняются не в транзакции. Два параллельных POST от одного пользователя могут оба увидеть count == 0 и оба попытаться вставить строку, что нарушит UNIQUE (user_id) и даст 500 одному из запросов.
Что сделать: обернуть чтение+запись в транзакцию с соответствующим уровнем блокировки, либо использовать INSERT ... ON CONFLICT (user_id) DO UPDATE (upsert одним запросом) вместо ручной проверки количества строк.
Затронутые файлы: handlers/profile.go.
