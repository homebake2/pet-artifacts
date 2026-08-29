---
id: 01ef1b5a-01cd-4b7e-aedc-232a8557b218
identifier: PET-63
type: Task
title: Дождаться ответа сервера перед переходом назад
state: Done
priority: medium
labels: [profile, frontend]
parent: PET-71
pages:
  - PET/pages/profile/redaktirovanie-profilya-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: после нажатия «Сохранить» экран сразу вызывает goBack(), не дожидаясь ответа — сохранение выглядит мгновенным и всегда успешным, даже если запрос впоследствии завершится ошибкой.
Что сделать: вызывать goBack() только после успешного ответа мутации; при ошибке — показывать сообщение и оставаться на форме, не теряя введённые пользователем данные.
Затронутые файлы: src/pages/profile-edit/profile-edit-connector.tsx, src/pages/profile-edit/profile-edit-form/profile-edit-form.tsx.
