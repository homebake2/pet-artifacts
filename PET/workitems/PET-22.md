---
id: 7f039ba9-ea0c-4f92-afb3-787271a826ab
identifier: PET-22
type: Task
title: Реализовать обновление access-токена (auto-refresh)
state: Done
priority: medium
labels: [auth, frontend]
parent: PET-68
pages:
  - PET/pages/auth/obnovlenie-tokena-frontend.md
  - PET/pages/auth/vhod-i-registratsiya-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: usePostRefresh определён, но нигде не используется. Нет интерцептора на 401, нет фонового обновления — через 14 дней (срок жизни access-токена) пользователь начнёт получать ошибки без объяснения.
Что сделать: добавить axios-интерцептор на privateAxiosInstance, который при 401 вызывает /auth/refresh с сохранённым refresh_token и повторяет исходный запрос с новым access_token. Учесть защиту от гонки: несколько параллельных 401 не должны запускать несколько параллельных /auth/refresh (сервер ротирует refresh-токен при каждом вызове — параллельные вызовы «погасят» друг друга).
Затронутые файлы: src/shared/api/config/instance.ts, src/shared/api/config/orval-mutator.ts, src/entities/auth/api/use-post-refresh.ts, src/entities/auth/hooks/use-get-session.tsx.
