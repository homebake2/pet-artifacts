---
id: 215a9f65-b4ad-4424-8ffa-ee8d32f37dc5
identifier: PET-40
type: Task
title: Скрыть мягко удалённых питомцев на всех эндпоинтах
state: Done
priority: medium
labels: [pets, backend]
parent: PET-69
pages:
  - PET/pages/pets/prosmotr-kartochki-pitomtsa-backend.md
  - PET/pages/pets/prosmotr-kartochki-pitomtsa-frontend.md
  - PET/pages/pets/redaktirovanie-pitomtsa-backend.md
  - PET/pages/pets/spisok-pitomtsev-backend.md
  - PET/pages/pets/udalenie-pitomtsa-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: GET /pet (список) фильтрует deleted_at IS NULL, а GET /pet/{id}, PUT /pet/{id} и DELETE /pet/{id} — нет. Мягко удалённый питомец пропадает из списка, но остаётся доступен для просмотра и редактирования по прямой ссылке/id.
Решение (принято): скрыть мягко удалённых питомцев везде — GET /pet/{id}, PUT /pet/{id} и DELETE /pet/{id} должны возвращать 404, если у питомца заполнен deleted_at, точно так же, как чужой/несуществующий питомец. Единая политика для всех эндпоинтов, фронтенду не нужно проверять флаг is_deleted отдельно.
Затронутые файлы: handlers/pet.go (добавить условие deleted_at IS NULL в запросы GetPetByIDAndProfileID/аналогичные, используемые GET/PUT/DELETE по id).
