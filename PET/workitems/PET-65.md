---
id: 09aed5ba-52a6-4ab0-91c8-c9de95ff5404
identifier: PET-65
type: Task
title: Исправить валидацию поля «Телефон»
state: Done
priority: medium
labels: [profile, frontend]
parent: PET-71
pages:
  - PET/pages/profile/redaktirovanie-profilya-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: поле хранится и валидируется как число — ввод символов вроде ведущего «+», пробелов, тире может некорректно преобразовываться в число без явной ошибки валидации.
Что сделать: хранить и валидировать телефон как строку на всех этапах (ввод/валидация/отправка), без Number()/parseInt(). Формат — regex ^\+?[0-9\s\-().]{1,20}$ (цифры, пробелы, дефисы, скобки, точки, один необязательный ведущий «+», длина до 20 символов), тот же паттерн должен использоваться на сервере (см. «Редактирование профиля — Backend», regexp.MustCompile того же выражения).
Затронутые файлы: src/entities/profile/schemas.ts (если есть), src/pages/profile-edit/profile-edit-form/profile-edit-form.tsx, src/pages/profile-edit/mappers/map-profile.ts.
