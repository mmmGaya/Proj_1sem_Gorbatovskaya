# найти индексы элементов списка, которые больше своего левого соседа, посчитать их количество
from random import randint

try:
    n = int(input("Введите размер списка: "))
    b = int(input("Введите любое целочисленное число: "))
except ValueError:
    print('error')
lst = [randint(0, b) for x in range(n)]

lst_indx = []

for i, x in enumerate(lst):
    if i > 0:
        if x > lst[i-1]:
            lst_indx.append(i)

print(f'Начальный списк: {lst}')
lst_indx.sort(reverse=True)
for i in lst_indx:
    print(i)
print(f'Количество чисел: {len(lst_indx)}')
