---
id: 3042a431-d189-48a2-8418-5947eab133f6
identifier: PET-72
type: Task
title: Инвалидировать access-токен при logout и удалении аккаунта
state: Done
priority: none
labels: []
parent: PET-68
pages:
  - PET/pages/auth/logout-backend.md
  - PET/pages/auth/logout-frontend.md
  - PET/pages/auth/obnovlenie-tokena-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: POST /auth/logout инвалидирует только refresh_token (обнуляет users.refresh_token). Уже выданный access_token остаётся валидным до истечения своего срока (14 дней), так как проверка подписи JWT не обращается к БД. Это значит, что похищенный или скомпрометированный access-токен продолжает работать после того, как пользователь вышел из аккаунта или удалил его. Требуется механизм отзыва, которого сейчас нет.
Решение (принято): без полноценного чёрного списка токенов (дорого при высокой нагрузке) — добавить пользователю колонку tokens_invalidated_at timestamptz. При успешном POST /auth/logout и при удалении аккаунта устанавливать tokens_invalidated_at = now(). В access-токен добавить claim iat (issued at, если ещё не используется). Middleware проверки access-токена на защищённых эндпоинтах должен читать tokens_invalidated_at пользователя (по id из токена) и отклонять токен с 401 UNAUTHORIZED, если его iat раньше tokens_invalidated_at. Это даёт серверную инвалидацию access-токена без внешнего хранилища чёрного списка, за счёт одного дополнительного запроса к БД на защищённый запрос (или кэша с TTL, если нагрузка потребует).
Затронутые файлы: database/migrations/ (новая миграция), utils/jwt.go, middleware/auth.go (или аналогичный файл проверки access-токена), handlers/auth.go (logout), обработчик удаления аккаунта.
