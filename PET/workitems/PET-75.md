---
id: ece4b6d8-4245-4bf3-8734-9c90758a1f08
identifier: PET-75
type: Task
title: Убрать поле is_deleted из запроса обновления питомца
state: Backlog
priority: none
labels: []
parent: PET-69
pages:
  - PET/pages/pets/redaktirovanie-pitomtsa-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: аналогично CreatePetRequest (см. задачу «Убрать поле is_deleted из запроса создания»), поле is_deleted присутствует в UpdatePetRequest (PUT /pet/{id}), но не имеет эффекта — статус удаления должен управляться только через DELETE /pet/{id}.
Решение (принято): убрать поле is_deleted из модели запроса обновления питомца — сервер не должен принимать и учитывать его в теле PUT /pet/{id}.
Затронутые файлы: models/pet.go (UpdatePetRequest), open-api/spec.json (UpdatePetRequest schema).
