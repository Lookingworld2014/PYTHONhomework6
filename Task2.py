# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input("Задаём минимум"))
max_number = int(input("Задаём максимум"))
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i)



#второй вариант

import random
listik = [random.randint(0, 100) for _ in range(10)]
print("Список:", my_list)
min_val = int(input("Задаём минимум"))
max_val = int(input("Задаём максимум"))
indices = [i for i in range(len(listik)) if min_val <= listik[i] <= max_val]
print(f"Индексы элементов, принадлежащих диапазону [{min_val}, {max_val}]:", indices)
