---
id: d9f02348-8cfc-48e7-9dba-0f5b54739323
identifier: PET-42
type: Task
title: Валидировать формат birth_date до вставки в БД
state: Done
priority: medium
labels: [pets, backend]
parent: PET-69
pages:
  - PET/pages/pets/dobavlenie-pitomtsa-backend.md
  - PET/pages/pets/redaktirovanie-pitomtsa-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: некорректный формат birth_date приводит к 500 (внутренняя ошибка от драйвера БД), а не к понятной 400-ошибке валидации.
Что сделать: явно парсить birth_date (формат YYYY-MM-DD) перед вставкой/обновлением и возвращать 400 VALIDATION_ERROR с понятным сообщением при ошибке парсинга.
Затронутые файлы: handlers/pet.go (создание и обновление питомца).
