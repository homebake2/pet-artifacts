---
id: 6744232e-58a0-4267-8a32-a52917363d5c
name: pet
states:
  - Backlog
  - Todo
  - In Progress
  - Done
  - Cancelled
labels:
  - frontend
  - backend
  - profile
  - calendar
  - pets
  - auth
  - concepts
  - admin
workitem_types:
  - Task
  - Epic
---

PetHealth — мобильное приложение для учёта здоровья домашних питомцев: профиль
владельца, карточки питомцев и календарь событий (приёмы, вакцинации,
лекарства и т.п.). Backend на Go (net/http, JWT-аутентификация, PostgreSQL),
фронтенд — мобильное приложение (React Native). API описан в
open-api/spec.json.
