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

weight, urine, defecation, vomit, diarrhea, other.
