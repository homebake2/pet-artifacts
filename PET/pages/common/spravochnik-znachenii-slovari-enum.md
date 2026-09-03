---
id: 247d2c19-2478-49dc-b7c7-192dbeaf4279
title: Справочник значений (словари enum)
workitems: []
created_at: 2026-08-24
updated_at: 2026-09-03
---
Единый справочник допустимых значений для полей-перечислений (enum), используемых в требованиях Pets и Calendar. Другие страницы требований должны ссылаться на этот документ вместо того, чтобы дублировать или расплывчато описывать списки значений.

## Питомцы — Вид (species / icon), 31 значение

DOG, CAT, HAMSTER, GUINEA_PIG, RABBIT, PARROT, CANARY, FISH, TURTLE, RAT, MOUSE, FERRET, HEDGEHOG, CHINCHILLA, MINI_PIG, MINI_GOAT, CHICKEN, DUCK, PIGEON, IGUANA, GECKO, BEARDED_AGAMA, SNAKE, PYTHON, FROG, AXOLOTL, TARANTULA, HERMIT_CRAB, ANT_FARM, SNAIL, OTHER.

## Питомцы — Пол (gender)

male, female, other.

## Питомцы — Тип содержания (habitation)

indoor, outside, both.

## Питомцы — Порода (breed)

На уровне API поле breed — свободный текст (не enum), список пород по видам на сервере не хранится. Если фронтенду нужен выпадающий список пород, зависящий от выбранного вида, — это отдельный клиентский справочник, который ещё не описан; требует отдельной проработки content-командой (см. открытый вопрос в задачах Pets).

## Календарь — Тип события (event type)

weight, temperature, feeding, water, activity, sleep, medication, hygiene, mood, urine, defecation, vomit, diarrhea, other.

Форма типизированного значения (`value`) по каждому типу события, а также характер значения и правила агрегации для графиков — см. [Модель значения события и реестр метрик](model-znacheniya-sobytiya-i-metriki.md). Enum ниже — вложенные словари полей `value`; они принадлежат конкретному типу события и не применяются к другим типам.

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

## Календарь — Вид активности (activity.kind)

walk, free_range, play, training, swim, other.

`free_range` — время вне клетки, вольера или террариума (свободный выгул птицы, грызуна, черепахи).

## Календарь — Единица дозы лекарства (medication.dose_unit)

mcg, mg, g, ml, drop, tablet, capsule.

`mcg` включён потому, что дозировки для мелких птиц и рептилий выражаются в микрограммах.

## Календарь — Процедура гигиены (hygiene.procedure)

bath, brushing, teeth, nails, beak, ears, shedding, antiparasitic, enclosure, water_change, other.

`beak` — уход за клювом и когтями птиц; `shedding` — помощь при линьке (в том числе купание рептилии при проблемной линьке); `enclosure` — уборка клетки, вольера, террариума или аквариума; `water_change` — подмена воды.

## Календарь — Состояние питомца (mood.state)

calm, playful, lethargic, anxious, aggressive, hiding.

`hiding` — питомец прячется и избегает контакта; для рептилий, грызунов и рыб это одно из основных наблюдаемых изменений поведения.

## Календарь — Статус выделений (urine / defecation / vomit / diarrhea — value.status)

normal, abnormal.

## Календарь — Интервал агрегации графика (bucket)

day, week, month.
