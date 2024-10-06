
# импортируем библиотеки
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# считываем файлы ексель
data = pd.read_excel("C:/Users/andre/Downloads/res_plast.xlsx")
data1 = pd.read_excel("C:/Users/andre/Downloads/wells_info.xlsx")
data.index += 1
data1.index += 1

# создаем словарь по двум условиям, где ключ - скважина, а значения - список давлений
target_year = 2020
value_to_check = 2
condition1 = data['Дата'].dt.year == target_year # условие по 2020 году
condition2 = data['Месторождение'].isin([value_to_check]) # условие по 2 месторождению
filtered_df = data[condition1 & condition2]
dictionary1 = filtered_df.groupby('Скважина')['Давление'].apply(list).to_dict()

# создаем второй словарь, где ключ - object, а значение - список давлений из первого словаря. 
dictionary2 = {}
for index, row in data1.iterrows():
    well = row['well']
    object_value = row['object']
    if well in dictionary1:
        # Добавление давления в список соответствующего объекта
        if object_value in dictionary2:
            dictionary2[object_value].extend(dictionary1[well])
        else:
            dictionary2[object_value] = dictionary1[well]
for key in dictionary2:
    dictionary2[key] = list((dictionary2[key]))
sorted_dict_by_keys = {k: dictionary2[k] for k in sorted(dictionary2)}

# создаем словарь, в котором подсчитаем среднее значение по объектам
average_dict = {}

# Проход по ключам и значениям в словаре
for key, values in dictionary2.items():
    # Фильтрация значений, исключение нулевых, отрицательных и нечисловых значений
    filtered_values = []
    for value in values:
        try:
            num = float(value)
            if num > 0 and num <1000:
                filtered_values.append(num)
        except ValueError:
            continue
    if filtered_values:  # Проверяем, что список не пустой после фильтрации
        average_dict[key] = round(sum(filtered_values) / len(filtered_values), 2) #округляем до двух знаков после запятой
    else:
        average_dict[key] = 0  # Если список пустой после фильтрации, среднее значение равно 0
sorted_dict_by_keys1 = {k: average_dict[k] for k in sorted(average_dict)}
for key, value in average_dict.items():
    print(f"Объект {key} Среднее значение: {value}")

keys = list(sorted_dict_by_keys1.keys())
values = list(sorted_dict_by_keys1.values())
plt.figure(figsize=(10, 6))  # Размер графика
plt.bar(keys, values, color='moccasin')
plt.xlabel('объект', fontsize=14)  # Подпись оси X
plt.ylabel('Средние давления', fontsize=14)  # Подпись оси Y
plt.title('Столбчатая диаграмма средних давлений', fontsize=16)  # Заголовок графика
plt.xticks(keys, fontsize=12)  # Настройка меток на оси X
plt.yticks(fontsize=12)  # Настройка меток на оси Y
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Добавление сетки по оси Y
plt.show()