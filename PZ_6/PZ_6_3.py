# обнулить элементы списка, располож. между его мин. и макс. элементами
from random import randint

n = int(input("Введите размер списка: ")) # try-except
b = int(input("Введите любое целочисленное число: "))

lst = [randint(0, b) for x in range(n)]
indx_max = lst.index(max(lst))
indx_min = lst.index(min(lst))
print(lst)

for i, x in enumerate(lst):
    if indx_max < i < indx_min or indx_min < i < indx_max:
        lst[i] = 0

print(lst)