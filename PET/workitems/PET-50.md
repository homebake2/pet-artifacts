---
id: 83f96f1c-5d50-4922-bf3a-28ab54ea8d42
identifier: PET-50
type: Task
title: Дождаться ответа сервера перед переходом назад при добавлении/редактировании питомца
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
Проблема: переход «назад» происходит до получения ответа от сервера — при сбое сохранения пользователь не узнает об этом и решит, что питомец добавлен/изменён.
Что сделать: переходить назад только после успешного ответа мутации; при ошибке — показывать сообщение и оставаться на форме.
Затронутые файлы: src/pages/add-pet/add-pet-connector.tsx, src/pages/pet-detail/pet-detail-controller.tsx (если там же редактирование).
