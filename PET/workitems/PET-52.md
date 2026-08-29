---
id: 145f6a24-5edf-45ee-ba81-26c724678227
identifier: PET-52
type: Task
title: Визуально различить режимы «добавление» и «редактирование»
state: Done
priority: medium
labels: [pets, frontend]
parent: PET-69
pages:
  - PET/pages/pets/dobavlenie-pitomtsa-frontend.md
  - PET/pages/pets/redaktirovanie-pitomtsa-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: заголовок экрана и текст кнопки одинаковы для обоих сценариев («Добавление питомца» / «Сохранить») — пользователь не всегда понимает, в каком режиме находится форма.
Что сделать: менять заголовок и/или текст кнопки в зависимости от режима (например, «Добавить питомца» vs «Изменить данные питомца»).
Затронутые файлы: src/pages/add-pet/add-pet.tsx, src/pages/pet-detail/pet-detail.tsx (если редактирование там же).
