---
id: b9f1063c-5496-41ef-a3c7-164503502134
identifier: PET-38
type: Task
title: Добавить состояния загрузки и ошибки на экран календаря
state: Done
priority: medium
labels: [calendar, frontend]
parent: PET-70
pages:
  - PET/pages/calendar/prosmotr-kalendarya-frontend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: нет визуальной индикации ошибки загрузки активностей (сетевой сбой, 500) — событие просто отсутствует в списке, неотличимо от «у питомца нет событий»; также нет индикатора «загрузка» на время выполнения useQueries.
Что сделать: добавить явные UI-состояния loading/error на экране календаря, использовать isLoading/isFetching/isError.
Затронутые файлы: src/pages/calendar/calendar.tsx, calendar-connector.tsx.
