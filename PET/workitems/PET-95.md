---
id: 8bd2bb3f-f5ce-42e7-91df-8a7689fdca3b
identifier: PET-95
type: Task
title: Блокировать кнопку «Войти» на время запроса
state: Done
priority: medium
labels: [auth, frontend]
parent: PET-88
pages:
  - PET/pages/auth/vhod-i-registratsiya-frontend.md
created_at: 2026-08-27
updated_at: 2026-08-30
---
Сейчас нет защиты от повторного тапа на кнопку входа — параллельные запросы могут привести к дублирующимся попыткам логина/регистрации. Нужно блокировать кнопку на время выполнения запроса, следуя общему UI-паттерну блокировки повторной отправки.
