---
id: 97b91a3a-a511-4bca-8661-215a730e9744
identifier: PET-53
type: Task
title: Показывать индикатор загрузки и блокировать повторную отправку формы
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
Проблема: нет индикатора «сохранение…» и блокировки кнопки «Сохранить» на время запроса — возможна повторная отправка при медленной сети.
Что сделать: дизейблить кнопку и показывать индикатор загрузки на время выполнения мутации создания/обновления питомца.
Затронутые файлы: src/pages/add-pet/form/add-pet-form/add-pet-form.tsx.
