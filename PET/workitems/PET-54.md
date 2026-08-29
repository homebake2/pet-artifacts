---
id: 64b72ffe-9fe8-4148-af96-4e6e0425c025
identifier: PET-54
type: Task
title: Показывать сообщение об ошибке при неудачном сохранении питомца
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
Проблема: нет уведомления пользователю при ошибке сохранения на сервере (сеть, 400, 500).
Что сделать: показывать snackbar/alert с текстом ошибки при onError мутации создания/обновления питомца.
Затронутые файлы: src/pages/add-pet/add-pet-connector.tsx, src/shared/ui/atoms/snackbar/*.
