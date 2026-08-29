---
id: 76802d75-d3f0-4698-8da4-38f98b8665f0
identifier: PET-45
type: Task
title: Убрать поле is_deleted из запроса создания
state: Done
priority: medium
labels: [pets, backend]
parent: PET-69
pages:
  - PET/pages/pets/dobavlenie-pitomtsa-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: is_deleted присутствует в CreatePetRequest, но не имеет эффекта при создании питомца.
Решение (принято): убрать поле из модели запроса на создание — клиент не должен присылать is_deleted при POST /pet, состояние удаления управляется только через DELETE /pet/{id}.
Затронутые файлы: models/pet.go (CreatePetRequest), open-api/spec.json (CreatePetRequest schema).
