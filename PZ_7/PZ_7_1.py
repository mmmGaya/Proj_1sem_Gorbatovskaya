# вывести символ с кодом равным N

try:
    n = int(input('Введите число в диапозоне от 32 до 126: '))
    print(chr(n))
except ValueError:
    print('Попробуйте еще раз:)')


