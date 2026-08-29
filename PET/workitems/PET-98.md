---
id: a4cc0d6f-45e5-44c7-b96a-32423ea9415d
identifier: PET-98
type: Task
title: Добавить rate limiting на регистрацию по IP (3 в день)
state: Done
priority: high
labels: [auth, backend]
parent: PET-89
pages:
  - PET/pages/auth/vhod-i-registratsiya-backend.md
created_at: 2026-08-27
updated_at: 2026-08-30
---
Единый эндпоинт login/register позволяет без ограничений "застолбить" чужой логин перебором и не имеет защиты от спама регистраций. Механизм (подробно — см. §3b "Rate limiting на регистрацию" на странице "Вход и регистрация — Backend"): отдельная таблица registration_rate_limit(ip inet, day date, count int, PK(ip,day)); IP берётся из X-Forwarded-For (первый адрес), fallback RemoteAddr; на шаге "login не найден, будет авто-регистрация" — атомарный upsert INSERT...ON CONFLICT(ip,day) DO UPDATE SET count=count+1 RETURNING count; если count > 3 — регистрация не выполняется, ответ 429 RATE_LIMITED; ошибка БД на этом шаге — fail closed (500), не пропускать регистрацию в обход лимита.
