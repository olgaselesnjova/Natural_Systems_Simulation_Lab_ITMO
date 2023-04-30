# Natural_Systems_Simulation_Lab_ITMO

**Role:** Data Analyst | Business Analyst at ITMO University, Laboratory of Artificial Intelligence

**Department:** National Center for Cognitive Technologies -> Natural Systems Simulation Lab

## **Tasks:** 
### 1. Comparative analysis of reanalysis currents and existing actual currents at the locations of floating autonomous base stations (FABS) by ice-free periods
### Folder: rozes
The data in the datasets has been edited.

**Technical requirements**

- The analysis should be carried out for the available observation dates from 2012.
- The analysis should include a comparison of data at locations FABS No. 1,11,12 (at depths of 3.4, 12.2, 25.4 m), PABS No. 5.10 (at depths of 3.4, 12.2, 25.4, 47.1 m).
- The analysis should be based on actual measurements averaged over the reanalysis horizons.

**Expected Results:**

- Uploading current data at FABS No. 1,5,10,11,12 (iceconc, vomecrty, vozocrtx).
- Analysis of currents with visualization in the format of velocity roses.

**Stages of analysis:**

**Task:** 

Perform a comparison:
By deserted periods - reanalysis currents and actual currents at the locations of PAS No.1,5,10 (Kara Sea) 12,11 (Laptev Sea) for the available observation dates from 2012. 
On the horizons:
- depths for regular FABS - 3.4, 12.2, 25.4 mm
- depths for deep-sea FABS 5.10 - additionally at 47.1m
The actual measurements lead to the horizons of reanalysis by averaging.
It is ineeded to represent comparison to estimate the modeling error of iceberg propagation during drift by using **rose of speeds**.







**Вход:** N столбцов модели (files in folder: model), K столбцов измерений (files in folder: parsed_measurements)

**Осреднение:**
- N столбцов модели (model)
- N столбцов измерений (меньше столбцов - в parsed_measurements нужно будет осреднить столбцы - если в реанализе (модели) горизонты вида (от 12 до 25) метров, то по всем горизонтам измерений внутри этого диапазона нужно взять среднее, то есть все измерения которые >=12 и <=25 можно осреднить по глубине по каждой дате = (я усреднила все столбцы - averaged_depths_(all))

Нужно проверить данные parsed_measurements и averaged_depths_(all) на одинак кол-во столбцов В DF, осталось ПАБС 5 проверить и решить, что делать с теми, у кого больше столбцов - скорее всего откинуть

**Фильтрация (убираем безледный период, где iceconc = 0 (Догрузить ПАБС 5)):** N столбцов модели (model - нужно догрузить [vozocrtx, vomecrty] для ПАБС 5), N столбцов измерений (меньше строк)

**Рисование роз:** розы модели и розы измерений (показывать на одном графике в сравнении) 




Подготовка требований к разработке алгоритмов и программного обеспечения для прогнозирования состояния льда в Арктике совместно с Арктическим научным центром "Роснефти".
Анализ данных гидрометеорологических условий.







### 2. ""По систематическому завышению температуры морской воды - мы все спорим, может в реанализе солености воды занижены?
### Folder: vosaline_votemper
Есть какие-то картинки по вертикальным профилям солености зимой, примерно в районе каких нибудь ПАБС? (раз там измеряли)
Помню в отчете только визуальное сравнение карт соленостей поверхностного слоя (там просто про численное моделирование, без
прогнозирования - рис 6.2.3)."
Нужно проверить это завышение.
Нужно нарисовать график где по Y - глубина, а по Х - значение солености. Данные взять из хранилища и осреднив за зиму. Соленость - это
переменная vosaline в nemo.
