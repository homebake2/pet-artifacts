---
id: 1c6356ab-c42a-439d-8041-13f65ddf6419
identifier: PET-74
type: Task
title: Инвалидировать кэш списка питомцев после создания и редактирования
state: Backlog
priority: none
labels: []
parent: PET-69
pages:
  - PET/pages/pets/dobavlenie-pitomtsa-frontend.md
  - PET/pages/pets/redaktirovanie-pitomtsa-frontend.md
  - PET/pages/pets/spisok-pitomtsev-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: в сетевом режиме кэш списка питомцев (React Query) не инвалидируется принудительно после успешного создания или редактирования питомца — список на экране «Питомцы» может не отразить изменения до следующего pull-to-refresh или повторного захода на экран.
Решение (принято): инвалидировать кэш списка питомцев (и кэш карточки конкретного питомца при редактировании) сразу после успешного ответа мутации создания/обновления, аналогично тому, как это должно быть сделано для удаления (см. задачу «Реализовать удаление питомца в интерфейсе»).
Затронутые файлы: src/entities/pet/api/use-create-pet.ts, src/entities/pet/api/use-update-pet.ts, src/entities/pet/api/queries.ts.
