---
id: cba37c21-f767-4ea1-9653-9df1063b4576
identifier: PET-47
type: Task
title: Реализовать удаление питомца в интерфейсе (главная задача)
state: Done
priority: medium
labels: [pets, frontend]
parent: PET-69
pages:
  - PET/pages/pets/prosmotr-kartochki-pitomtsa-frontend.md
  - PET/pages/pets/spisok-pitomtsev-frontend.md
  - PET/pages/pets/udalenie-pitomtsa-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: backend полностью поддерживает DELETE /pet/{id} (мягкое удаление, проверка владения, покрыт тестами), но в приложении нет ни кнопки, ни свайпа, ни диалога подтверждения — хук useDeletePet существует, но нигде не вызывается.
Решение (принято): реализовать в этой итерации. Добавить точку входа для удаления (кнопку/свайп на карточке в списке питомцев или на экране деталей — по аналогии с уже реализованным свайп-удалением события, см. requirments/calendar/udalenie-sobytiya/frontend.md как референс паттерна), диалог подтверждения, обработку ошибок и обновление списка после успешного удаления (с инвалидацией кэша списка питомцев).
Затронутые файлы: src/entities/pet/api/use-delete-pet.ts, src/pages/pets/pets.tsx, src/pages/pet-detail/pet-detail.tsx, src/shared/ui/molecules/pet-card/pet-card.tsx.
