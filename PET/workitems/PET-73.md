---
id: ba2be13b-7fb6-42bf-b503-7a61bcfd97ec
identifier: PET-73
type: Task
title: Задокументировать в OpenAPI фактическое поведение 405 для GET /profile
state: Backlog
priority: none
labels: []
parent: PET-71
pages:
  - PET/pages/profile/prosmotr-profilya-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: open-api/spec.json не описывает ответ 405 Method Not Allowed для GET /profile, хотя код его реально возвращает при обращении неподходящим методом. При этом 405 использует код ошибки BAD_REQUEST вместо отдельного значения в ErrorCodeEnum.
Решение (принято, по аналогии с задачей №18 для auth-эндпоинтов): добавить 405 в спецификацию для /profile с телом {code: BAD_REQUEST, message: "Method not allowed"}; отдельный код METHOD_NOT_ALLOWED не заводить — переиспользование BAD_REQUEST фиксируется как осознанное решение (низкий приоритет, не влияет на клиентскую логику).
Затронутые файлы: open-api/spec.json.
