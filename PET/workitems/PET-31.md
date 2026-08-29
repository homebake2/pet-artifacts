---
id: db2795bc-1786-4be5-a74b-2c72bdf00b80
identifier: PET-31
type: Task
title: Разрешить удаление события у мягко удалённого питомца — оставить как есть
state: Done
priority: medium
labels: [calendar, backend]
parent: PET-70
pages:
  - PET/pages/calendar/udalenie-sobytiya-backend.md
created_at: 2026-08-24
updated_at: 2026-08-30
---
Проблема: POST /events и PUT /events/{id} запрещают операцию для мягко удалённого питомца, а DELETE /events/{id} — нет.
Решение (принято): текущее поведение сохраняется осознанно — удаление событий у мягко удалённого питомца разрешено (полезно для очистки истории даже после удаления питомца). Изменений не требуется, зафиксировать в OpenAPI как явное поведение, а не как недосмотр.
Затронутые файлы: open-api/spec.json (уточнить описание DELETE /events/{id}).
