---
id: 7d2c56b1-164c-4a49-a948-a1850b708cea
identifier: PET-18
type: Task
title: Задокументировать в OpenAPI фактическое поведение 405
state: Done
priority: medium
labels: [auth, backend]
parent: PET-68
pages:
  - PET/pages/auth/logout-backend.md
  - PET/pages/auth/obnovlenie-tokena-backend.md
  - PET/pages/auth/vhod-i-registratsiya-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: open-api/spec.json не описывает ответ 405 Method Not Allowed ни для одного auth-эндпоинта (/auth/login, /auth/register, /auth/refresh, /auth/logout), хотя код его реально возвращает. При этом 405 использует код ошибки BAD_REQUEST вместо отдельного значения в ErrorCodeEnum.
Решение (принято): добавить 405 в спецификацию для всех четырёх путей с телом {code: BAD_REQUEST, message}; отдельный код METHOD_NOT_ALLOWED не заводить — переиспользование BAD_REQUEST фиксируется как осознанное решение (низкий приоритет, не влияет на клиентскую логику).
Затронутые файлы: open-api/spec.json.
