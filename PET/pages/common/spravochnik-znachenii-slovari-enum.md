---
id: 247d2c19-2478-49dc-b7c7-192dbeaf4279
title: Справочник значений (словари enum)
created_at: 2026-08-24
updated_at: 2026-10-20
---
Единый справочник допустимых значений для полей-перечислений (enum), используемых в требованиях Pets и Calendar. Другие страницы требований должны ссылаться на этот документ вместо того, чтобы дублировать или расплывчато описывать списки значений.

## Питомцы — Вид (species), 31 значение

DOG, CAT, HAMSTER, GUINEA_PIG, RABBIT, PARROT, CANARY, FISH, TURTLE, RAT, MOUSE, FERRET, HEDGEHOG, CHINCHILLA, MINI_PIG, MINI_GOAT, CHICKEN, DUCK, PIGEON, IGUANA, GECKO, BEARDED_AGAMA, SNAKE, PYTHON, FROG, AXOLOTL, TARANTULA, HERMIT_CRAB, ANT_FARM, SNAIL, OTHER.

## Питомцы — Пол (gender)

male, female, other.

## Питомцы — Тип содержания (habitation)

indoor, outside, both.

## Питомцы — Тип воды (water_type)

freshwater, saltwater.

Профильное поле группы видов «Водные и полуводные» (`FISH`, `AXOLOTL`, `FROG`, `TURTLE`) — см. [Профильные поля питомца по видам](../pets/profilnye-polya-pitomtsa-po-vidam.md).

## Питомцы — Порода (breed)

На уровне API поле breed — свободный текст (не enum), список пород по видам на сервере не хранится. Если фронтенду нужен выпадающий список пород, зависящий от выбранного вида, — это отдельный клиентский справочник, который ещё не описан; требует отдельной проработки content-командой (см. открытый вопрос в задачах Pets).

## Календарь — Тип события (event type)

weight, temperature, feeding, water, activity, sleep, medication, hygiene, mood, urine, defecation, vomit, diarrhea, other, molting, egg_laying, water_quality, heat_cycle, vaccination.

`vaccination` — системный тип: создаётся флоу «Вакцинации» (факт введения, напоминание на следующую вакцинацию и дополнительные напоминания) и не предлагается в ручном выборе типа события; см. [Модель значения события и реестр метрик](model-znacheniya-sobytiya-i-metriki.md), раздел «Типы, создаваемые системой».

Форма типизированного значения (`value`) по каждому типу события, а также характер значения и правила агрегации для графиков — см. [Модель значения события и реестр метрик](model-znacheniya-sobytiya-i-metriki.md). Enum ниже — вложенные словари полей `value`; они принадлежат конкретному типу события и не применяются к другим типам.

Не каждый тип события применим к каждому виду питомца из справочника видов ниже — состав видов, которым доступен конкретный тип, задан таблицей «Применимость типа события к виду питомца» на странице [Модель значения события и реестр метрик](model-znacheniya-sobytiya-i-metriki.md).

Словари ниже наполняются с учётом всех видов справочника видов питомцев, а не только собак и кошек: распространённые для нескольких видов случаи — отдельные значения, узкоспецифичные — значение `other` плюс пояснение в `notes` (правило см. [Модель значения события и реестр метрик](model-znacheniya-sobytiya-i-metriki.md), раздел «Разнообразие видов и состав словарей»).

## Календарь — Вид замера температуры (temperature.kind)

body, environment.

`body` — температура тела питомца; `environment` — температура среды обитания (террариум, точка прогрева, вода аквариума), которая для рептилий, амфибий и рыб и является предметом наблюдения.

## Календарь — Единица измерения кормления (feeding.unit)

g, ml, portion, piece.

`piece` — счётные корма: кормовые грызуны, насекомые, мальки («2 мыши», «10 сверчков»).

## Календарь — Вид корма (feeding.food)

dry, wet, raw, homemade, live_prey, frozen_prey, insects, hay, grain, greens, treat, other.

`live_prey` — живой кормовой объект (грызуны, рыба); `frozen_prey` — размороженный кормовой грызун; `insects` — насекомые и их личинки; `hay` — сено и грубые корма; `grain` — зерно и семена; `greens` — зелень, овощи и фрукты; `other` — всё, что не покрыто перечисленным, с пояснением в `notes`.

Не каждое значение применимо к каждому виду питомца, которому применим сам тип `feeding` — см. [Модель значения события и реестр метрик](model-znacheniya-sobytiya-i-metriki.md), раздел «Применимость значений вложенных словарей `value` к виду питомца», таблица `feeding.food`.

## Календарь — Вид активности (activity.kind)

walk, free_range, play, training, swim, other.

`free_range` — время вне клетки, вольера или террариума (свободный выгул птицы, грызуна, черепахи).

Не каждое значение применимо к каждому виду питомца, которому применим сам тип `activity` — см. [Модель значения события и реестр метрик](model-znacheniya-sobytiya-i-metriki.md), раздел «Применимость значений вложенных словарей `value` к виду питомца», таблица `activity.kind`.

## Календарь — Единица дозы лекарства (medication.dose_unit)

mcg, mg, g, ml, drop, tablet, capsule.

`mcg` включён потому, что дозировки для мелких птиц и рептилий выражаются в микрограммах.

## Календарь — Процедура гигиены (hygiene.procedure)

bath, brushing, teeth, nails, beak, ears, shedding, antiparasitic, enclosure, water_change, other.

`beak` — уход за клювом и когтями птиц; `shedding` — помощь при линьке (в том числе купание рептилии при проблемной линьке); `enclosure` — уборка клетки, вольера, террариума или аквариума; `water_change` — подмена воды.

Не каждое значение применимо к каждому виду питомца, которому применим сам тип `hygiene` (применим ко всем видам) — например, `brushing` (расчёсывание шерсти) неприменимо к `FISH`. См. [Модель значения события и реестр метрик](model-znacheniya-sobytiya-i-metriki.md), раздел «Применимость значений вложенных словарей `value` к виду питомца», таблица `hygiene.procedure`.

## Календарь — Состояние питомца (mood.state)

calm, playful, lethargic, anxious, aggressive, hiding.

`hiding` — питомец прячется и избегает контакта; для рептилий, грызунов и рыб это одно из основных наблюдаемых изменений поведения.

## Календарь — Статус выделений (urine / defecation / vomit / diarrhea — value.status)

normal, abnormal.

## Календарь — Статус линьки (molting.status)

started, stuck, completed.

`started` — линька началась; `completed` — линька завершена без осложнений; `stuck` — застрявшая (неполная) линька — тревожный признак, требующий внимания владельца (типично для рептилий и линяющих беспозвоночных).

## Календарь — Статус кладки (egg_laying.status)

normal, abnormal.

`abnormal` — осложнённая кладка (в т.ч. застрявшее яйцо) — ветеринарно значимое отклонение, а не просто заметка.

## Календарь — Фаза течки (heat_cycle.phase)

started, ended.

## Календарь — Интервал агрегации графика (bucket)

day, week, month.

## Ветпаспорт — Статус заболевания (disease.status)

active, cured.

## Ветпаспорт — Степень тяжести аллергии (allergy.severity)

mild, moderate, severe.

## Ветпаспорт — Кондиция (pet.body_condition)

underweight, thin, normal, overweight, obese.

Пятибалльная шкала телосложения (body condition score), упрощённая до пяти значений: `underweight` — истощение, `thin` — ниже нормы, `normal` — норма, `overweight` — избыточный вес, `obese` — ожирение. См. [Кондиция — Backend](../vetpassport/konditsiya-backend.md).

## Ветпаспорт — Статус вакцинации (computed, не хранится)

overdue, soon, current, completed.

Не enum-поле модели данных — вычисляется на клиенте из `vaccination.next_date` относительно текущей даты (см. [Вакцинации — Frontend](../vetpassport/vaktsinatsii-frontend.md)): `overdue` — `next_date` в прошлом, `soon` — в пределах 30 дней включительно, `current` — позже; `completed` — задан `vaccination.completed_at` (вакцинация завершена отметкой «Выполнено» напоминания на следующую вакцинацию). Записан здесь для единообразия с остальными словарями страницы, а не потому что backend валидирует или хранит это значение.

## Передача питомца — Статус (status)

pending, accepted, declined, cancelled, expired.

Поле `pet_transfer.status`; `pending` — передача создана и ожидает решения получателя, остальные значения конечные: принята, отклонена получателем, отменена отправителем (в том числе при удалении питомца) и истёк срок действия кода. Переходы и правила — см. [Передача питомца — Backend](../pets/peredacha-pitomtsa-backend.md).

## Доступ к питомцу — Роль (access)

owner, full, view.

Поле `access` в ответах `GET /pet` и `GET /pet/{id}` — роль текущего пользователя по отношению к питомцу: `owner` — владелец (`pet.user_id`), `full` — полный доступ, `view` — только просмотр. В таблице `pet_access.role` и в теле `POST /pet/{id}/access-invites` допустимы только `full` и `view`: `owner` не выдаётся. Права ролей — см. [Общие требования: Доступ к питомцу](obschie-trebovaniya-dostup-k-pitomtsu.md).

## Доступ к питомцу — Причина потери доступа (reason)

revoked, pet_deleted, pet_transferred.

Поле `pet_access_notice.reason` и элементов `access_lost` в ответе `GET /pet`: `revoked` — владелец отозвал доступ, `pet_deleted` — владелец удалил питомца или аккаунт, `pet_transferred` — питомец передан другому владельцу. Отказ участника от доступа уведомления не создаёт. См. [Доступ к питомцу — Backend](../pets/dostup-k-pitomtsu-backend.md).

## Доступ к питомцу — Статус приглашения (status)

pending, accepted, declined, cancelled, expired.

Поле `pet_access_invite.status`; значения и переходы те же, что у статуса передачи (см. выше), но для приглашения к доступу: `accepted` — доступ выдан, `cancelled` — отменено владельцем (в том числе при удалении питомца и при принятии передачи питомца). См. [Доступ к питомцу — Backend](../pets/dostup-k-pitomtsu-backend.md).
