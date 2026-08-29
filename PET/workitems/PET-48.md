---
id: a1fd6fe1-9058-4562-ad9f-5fcd76d0bc0b
identifier: PET-48
type: Task
title: Флаг is_deleted на карточке питомца — действие не требуется
state: Done
priority: medium
labels: [pets, frontend]
parent: PET-69
pages:
  - PET/pages/pets/prosmotr-kartochki-pitomtsa-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема (изначальная): предполагалось, что backend может отдавать GET /pet/{id} для мягко удалённого питомца, и фронтенду нужно бы отдельно проверять флаг is_deleted.
Решение (принято): после выполнения pets-backend.md, п.1 (скрытие мягко удалённых питомцев на всех эндпоинтах, включая GET /pet/{id}) сервер будет возвращать 404 для удалённого питомца вместо его данных — фронтенду достаточно обработать 404 как обычную ошибку «питомец не найден» (см. задачу №3), отдельная обработка флага is_deleted не нужна.
