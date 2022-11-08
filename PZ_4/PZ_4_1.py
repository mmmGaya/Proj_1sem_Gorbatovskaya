#вывети в порядке убыввания числа расположенные между a и b, также кол-во этих чисел
try:
    a, b = map(int, input('Введите два числа').split())
    n = 0
    for i in range(b-1, a, -1):
        n += 1
        print(i)
    print(f'Всего чисел между a и b: {n}')
except ValueError:
    print('Неверный тип данных')