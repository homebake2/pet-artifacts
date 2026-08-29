---
id: 151cd89c-d586-4207-ac01-8f21395ea623
identifier: PET-61
type: Task
title: Дополнить спецификацию ответом 500 для GET /profile
state: Done
priority: medium
labels: [profile, backend]
parent: PET-71
pages:
  - PET/pages/profile/prosmotr-profilya-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: в OpenAPI путь /profile (GET) не описывает 500 INTERNAL_ERROR, хотя код реально может его вернуть.
Что сделать: добавить 500 в описание ответов эндпоинта.
Затронутые файлы: open-api/spec.json.
