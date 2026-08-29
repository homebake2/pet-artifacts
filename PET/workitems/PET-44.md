---
id: 03aaf3e4-80d3-44a7-bacb-93c2de6433ba
identifier: PET-44
type: Task
title: Убрать обязательность LanguageCode
state: Done
priority: medium
labels: [pets, backend]
parent: PET-69
pages:
  - PET/pages/pets/dobavlenie-pitomtsa-backend.md
  - PET/pages/pets/prosmotr-kartochki-pitomtsa-backend.md
  - PET/pages/pets/redaktirovanie-pitomtsa-backend.md
  - PET/pages/pets/spisok-pitomtsev-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: заголовок LanguageCode обязателен и валидируется на GET-эндпоинтах питомцев, но не проверяется при создании/редактировании — несогласованность в рамках одного контроллера; при этом заголовок фактически не используется для локализации содержимого ответа (сервер не хранит переводов).
Решение (принято): убрать требование обязательности LanguageCode со всех эндпоинтов питомцев — заголовок ни на что не влияет в текущей реализации, поддерживать его как обязательный только ради валидации формата бессмысленно. Если локализация ответов сервера понадобится в будущем — заводить это отдельной задачей с реальной реализацией, а не пустой проверкой заголовка.
Затронутые файлы: handlers/pet.go, open-api/spec.json (убрать заголовок из списка обязательных параметров GET-эндпоинтов питомцев).
