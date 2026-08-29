---
id: 45cff75c-c2e5-4d67-863f-9924698b7b0d
identifier: PET-51
type: Task
title: Усилить обязательность поля «Вид» на форме
state: Done
priority: medium
labels: [pets, frontend]
parent: PET-69
pages:
  - PET/pages/pets/dobavlenie-pitomtsa-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: обязательность поля «Вид» (species) не гарантирована схемой клиентской валидации, хотя бэкенд требует его обязательно (см. pets-backend.md).
Что сделать: добавить явную обязательную валидацию поля в форме добавления/редактирования питомца, синхронизировав сообщение об ошибке с бэкенд-ограничением.
Затронутые файлы: src/entities/pet/schemas.ts, src/pages/add-pet/form/add-pet-form/add-pet-form.tsx.
