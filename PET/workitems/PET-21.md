---
id: 1e9c6ff2-3fae-466d-a1aa-b5bfcfa8ffdb
identifier: PET-21
type: Task
title: Реализовать реальный вызов logout на сервере
state: Done
priority: medium
labels: [frontend, auth]
parent: PET-68
pages:
  - PET/pages/auth/logout-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: кнопка «Выйти» сбрасывает только локальный $currentUser, но нигде не вызывает usePostLogout/postLogout (мёртвый код) и не очищает $tokens/заголовок Authorization на privateAxiosInstance. Refresh-токен пользователя остаётся действительным на сервере.
Что сделать: при нажатии «Выйти» вызывать POST /auth/logout с сохранённым refresh_token, дожидаться ответа (или хотя бы не блокировать выход при ошибке сети, но пытаться отправить запрос), затем сбрасывать $currentUser, $tokens и Authorization-заголовок.
Затронутые файлы: src/entities/auth/api/use-post-logout.ts, src/pages/settings/settings.tsx / settings-connector.tsx, src/entities/auth/hooks/*.
