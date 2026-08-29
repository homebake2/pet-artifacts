---
id: b56f2d0b-ef06-4db3-90d1-9a761bc528a6
identifier: PET-77
type: Task
title: Сделать удаление события мягким (soft delete), а не физическим
state: Backlog
priority: none
labels: [calendar, backend]
parent: PET-70
created_at: 2026-08-24
updated_at: 2026-08-24
---
Источник: страница «Удаление события — Backend». По результатам ревью требование изменено: DELETE /events/{id} теперь выполняет мягкое удаление (устанавливает event.deleted_at = now()) вместо физического удаления строки — по аналогии с мягким удалением питомцев. Все эндпоинты, читающие события (GET /activities, GET /events/{id} и т.п.), должны фильтровать по deleted_at IS NULL. Требуется реализовать миграцию/колонку, логику мягкого удаления в хендлере DELETE и фильтрацию во всех читающих запросах.
