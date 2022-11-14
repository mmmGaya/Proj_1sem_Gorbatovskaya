# найти номера элементов списка, которые больше своего левого соседа, посчитать их количество
from random import randint

n = int(input("Введите размер списка: ")) # try-except
b = int(input("Введите любое целочисленное число: "))

lst = [randint(0, b) for x in range(n)]

lst_indx = []
just_list = []
for i, x in enumerate(lst):
    if i > 0:
        if x > lst[i-1]:
            lst_indx.append(i)
            just_list.append(x)

print(f'Вывод начального списка: {lst}')
lst_indx.sort(reverse=True)
for i in lst_indx:
    print(i)
print(f'Количество чисел: {len(lst_indx)}')









