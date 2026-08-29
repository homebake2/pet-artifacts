---
id: 92b2974e-474d-4fb7-a0bb-b60b54975245
identifier: PET-43
type: Task
title: Требовать обязательность name/species только при создании, не при каждом PUT
state: Done
priority: medium
labels: [pets, backend]
parent: PET-69
pages:
  - PET/pages/pets/redaktirovanie-pitomtsa-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: PUT /pet/{id} требует непустые name и species в каждом запросе, хотя UpdatePetRequest спроектирован как частичное обновление (nullable-поля) — нельзя обновить только одно поле, например заметки, не передав повторно имя и вид.
Что сделать: убрать безусловное требование name/species на PUT; обновлять только переданные поля, как и остальные nullable-поля запроса.
Затронутые файлы: handlers/pet.go.
