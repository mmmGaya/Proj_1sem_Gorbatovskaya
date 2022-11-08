# определить имеется ли в записи числа нечетные цифры
try:
    n = int(input("Введите любое число: "))
    unev = False
    while n != 0:
        if (n % 10) % 2 != 0:
            unev = True
        n //= 10
    print(unev)
except ValueError:
    print('Неверный тип данных')