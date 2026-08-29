---
id: 67af0e4d-0cd8-4357-933c-22f5776f80b7
identifier: PET-23
type: Task
title: Персистить токены в защищённом хранилище
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
Проблема: currentUser (включая пароль в открытом виде) сохраняется в AsyncStorage, а $tokens — нет. После холодного перезапуска приложение показывает пользователя «вошедшим», но все приватные запросы уходят без Authorization.
Решение (принято): хранить access_token/refresh_token в защищённом нативном хранилище (Keychain на iOS / Keystore на Android — например, через react-native-keychain), не в обычном AsyncStorage. При старте приложения читать токены из этого хранилища и восстанавливать $tokens. Одновременно перестать хранить пароль пользователя в открытом виде в currentUser — он не нужен после успешного логина.
Затронутые файлы: src/entities/auth/hooks/use-get-auth.tsx, use-get-session.tsx, use-get-user.ts, src/entities/auth/domain.ts, добавить новую зависимость для secure storage, обновить package.json.
