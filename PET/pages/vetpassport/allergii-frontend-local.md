---
id: d237065c-adb6-4150-94d7-109b67f338ae
title: Аллергии — Frontend (dataSource=local)
parent_page: PET/pages/vetpassport/index.md
workitems: []
created_at: 2026-09-09
updated_at: 2026-09-09
---
## Смотрите также

* [Аллергии — Frontend](allergii-frontend.md) — общий сценарий; эта страница описывает только ветку `dataSource=local`.

* [Аллергии — Backend](allergii-backend.md)

* [Локальный режим (dataSource=local) — общая архитектура хранения](../common/lokalnyi-rezhim-datasource-local-zaglushka.md) — модель хранения, коллекция «Аллергии».

## Модель хранения

Отдельная коллекция «Аллергии», ключ `id` (UUID v4), партиционирование по `ownerId`, вторичный доступ по `petId`. Поля: `petId`, `allergen`, `reaction`, `detectedDate`, `severity`, `note`, `files` (массив, до 10 элементов), `isDeleted`, `deletedAt`.

## Алгоритм сохранения

1. Клиентская валидация — тот же набор правил, что на странице «Аллергии — Frontend».

2. Создание/редактирование — обычная запись/частичное обновление. Удаление — мягкое (`isDeleted: true`, `deletedAt`).

3. Кнопка «Сохранить»/«Удалить» блокируется на время записи.

## Обработка ошибок

Ошибка записи в локальное хранилище — тем же способом, что и сбой сохранения в сетевом режиме.

## Перенос local → network

Каждая неудалённая локальная аллергия переносится элементом `allergies` тела `POST /import/local-data` (см. «Импорт локальных данных — Backend», раздел о переносе Ветпаспорта).
