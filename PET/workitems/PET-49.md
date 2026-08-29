---
id: 4a9113fd-cc94-4afb-a451-09f5f1f17c46
identifier: PET-49
type: Task
title: Добавить состояния загрузки и ошибки на экран списка и деталей питомца
state: Done
priority: medium
labels: [pets, frontend]
parent: PET-69
pages:
  - PET/pages/pets/prosmotr-kartochki-pitomtsa-frontend.md
  - PET/pages/pets/spisok-pitomtsev-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: ни на экране списка (pets.tsx), ни на экране деталей (pet-detail.tsx) нет индикации загрузки — пользователь не может отличить «загружается» от «нет питомцев»/«ошибка».
Что сделать: добавить явные UI-состояния loading/error/empty на обоих экранах, использовать isLoading/isError из React Query.
Затронутые файлы: src/pages/pets/pets.tsx, pets-controller.tsx, src/pages/pet-detail/pet-detail.tsx, pet-detail-controller.tsx.
