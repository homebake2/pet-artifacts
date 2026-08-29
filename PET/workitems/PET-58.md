---
id: 66240419-274b-4811-9dda-060cb316869c
identifier: PET-58
type: Task
title: Задокументировать в OpenAPI разницу между POST и PUT
state: Done
priority: medium
labels: [profile, backend]
parent: PET-71
pages:
  - PET/pages/profile/redaktirovanie-profilya-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: спецификация описывает оба метода одной и той же схемой GetProfileRequest, не поясняя, что POST — «создать или полностью перезаписать», а PUT — «частично обновить существующий профиль».
Что сделать: явно развести описания POST и PUT в open-api/spec.json (описание, какие поля обязательны для каждого метода, поведение при отсутствии профиля).
Затронутые файлы: open-api/spec.json.
