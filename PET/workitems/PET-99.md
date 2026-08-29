---
id: f0c9a42a-d74d-47d1-8e62-77bf7d86e97a
identifier: PET-99
type: Task
title: Исправить гонку при одновременной регистрации одного login
state: Done
priority: high
labels: [auth, backend]
parent: PET-89
pages:
  - PET/pages/auth/vhod-i-registratsiya-backend.md
created_at: 2026-08-27
updated_at: 2026-08-30
---
При параллельных запросах с одинаковым новым login оба могут пройти проверку "пользователь не найден" и попытаться создать запись — второй INSERT падает с нарушением уникальности. Сервер обязан распознавать именно этот случай, а не любую ошибку INSERT, по коду ошибки PostgreSQL 23505 (unique_violation): для драйвера pgx — var pgErr *pgconn.PgError; errors.As(err, &pgErr) && pgErr.Code == "23505"; для database/sql поверх lib/pq — приведение err.(*pq.Error) и проверка .Code == "23505". Только при совпадении именно этого кода сервер должен трактовать ошибку как переход к сценарию "пользователь уже есть" (повторный поиск и сравнение пароля), а не как внутреннюю ошибку 500; любая другая ошибка INSERT обрабатывается как обычная ошибка БД (500 INTERNAL_ERROR).
