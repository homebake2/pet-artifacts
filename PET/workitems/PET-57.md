---
id: e95b35f9-a3b3-4518-9ebf-f35894c9df08
identifier: PET-57
type: Task
title: Разрешить частичное обновление через PUT без обязательного first_name
state: Done
priority: medium
labels: [profile, backend]
parent: PET-71
pages:
  - PET/pages/profile/redaktirovanie-profilya-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: PUT спроектирован как частичное обновление (поля — *string), но валидация всё равно требует непустой first_name в каждом запросе — нельзя обновить только телефон, не отправив заново имя.
Что сделать: убрать безусловное требование first_name для PUT; проверять только, что хотя бы одно поле передано (текущая ветка «ни одного поля не передано» сейчас недостижима из-за обязательного first_name — после фикса она должна реально обрабатываться и возвращать 400).
Затронутые файлы: handlers/profile.go.
