---
id: 7ac89a1c-d4f5-460d-b7cf-3e25097e688b
identifier: PET-60
type: Task
title: Гарантировать непустой login в ответе GET /profile
state: Done
priority: medium
labels: [profile, backend]
parent: PET-71
pages:
  - PET/pages/profile/prosmotr-profilya-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: GetMasterProfileResponse.login помечено как обязательное непустое поле, но код может вернуть пустую строку, если запись пользователя не найдена в users.
Решение (принято): гарантировать в коде, что login всегда непустой, а не ослаблять контракт спецификации. Раз строка profile физически не может существовать без соответствующего users (внешний ключ user_id REFERENCES users(id)), пустой login означает ошибку выполнения запроса (например, некорректный JOIN) — в этом случае возвращать 500 INTERNAL_ERROR, а не 200 с пустым полем.
Затронутые файлы: handlers/profile.go.
