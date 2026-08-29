---
id: 872eafb4-0ac0-402f-8e94-1e73a541951a
identifier: PET-97
type: Task
title: Создавать гостевого пользователя на бэкенде с рандомным логином и флагом is_guest
state: Done
priority: high
labels: [auth, backend]
parent: PET-89
pages:
  - PET/pages/auth/vhod-i-registratsiya-backend.md
  - PET/pages/auth/vhod-i-registratsiya-frontend.md
created_at: 2026-08-27
updated_at: 2026-08-30
---
Отдельный эндпоинт POST /auth/guest создаёт или находит гостевого пользователя по идентификатору устройства/сессии, минуя обычный флоу login/password. Тело запроса — одно поле device_id (string, обязательно, непусто); поиск ведётся по колонке guest_device_id, на которую строится уникальный частичный индекс (CREATE UNIQUE INDEX ... WHERE guest_device_id IS NOT NULL), чтобы обычные пользователи с guest_device_id = NULL не конфликтовали друг с другом. Алгоритм — два явных ветвления: если запись с таким guest_device_id найдена, используется её id как userId без создания новой строки (повторный вызов с тем же device_id не должен плодить дубликаты); если не найдена — создаётся новая запись. Логин генерируется как guest_ через crypto/rand, пароль не задаётся, у записи выставляется флаг is_guest=true. Миграция гостя в постоянный аккаунт — отдельная будущая фича, в этой задаче не реализуется.
