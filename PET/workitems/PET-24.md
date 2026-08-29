---
id: 6ba62349-7473-4380-a838-de3d155f7ab4
identifier: PET-24
type: Task
title: Реализовать полноценное удаление аккаунта
state: Done
priority: medium
labels: [auth, frontend]
parent: PET-68
pages:
  - PET/pages/auth/logout-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: пункт «Удалить аккаунт» в настройках ничего не удаляет и дублирует logout; отдельного API-эндпоинта удаления аккаунта в проекте нет ни в спецификации, ни на бэкенде.
Решение (принято): реализовать реальное удаление. Требует нового backend-эндпоинта (например, DELETE /profile или DELETE /account), который каскадно удаляет профиль/питомцев/события пользователя (либо переиспользует существующий каскад ON DELETE CASCADE от users — см. database/migrations) и инвалидирует refresh-токен. На фронте: диалог подтверждения (двойное подтверждение, т.к. действие необратимо), вызов нового эндпоинта, затем полный сброс сессии (как при logout) и переход на экран входа.
Затронутые файлы: src/pages/settings/settings.tsx, src/pages/settings/ui/settings-block/*, новый API-хук (по аналогии с use-post-logout.ts), src/shared/api/codegen/api/*.
Примечание: соответствующая backend-задача заведена отдельно — см. tasks/auth-backend.md (добавить новый пункт при планировании работы бэка).
