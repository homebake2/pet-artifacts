---
id: 7ef2dc6e-3898-4b14-bd55-864b90ba7c9c
identifier: PET-41
type: Task
title: Валидировать enum-значения gender и habilitation
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
Проблема: icon валидируется против списка допустимых значений (allowedIcons), а gender и habilitation — нет, хотя оба задуманы как перечисления (GetGenderEnum, GetHabilitationEnum). В БД можно сохранить произвольную строку.
Что сделать: добавить аналогичные allowedGenders/allowedHabilitations map и проверки в CreatePetRequest/UpdatePetRequest, возвращать 400 VALIDATION_ERROR при недопустимом значении.
Затронутые файлы: models/pet.go, handlers/pet.go.
