
# нахождение стоимости 1 кг конфет и 1 кг ирисок, также во сколько раз конфеты стоят больше ирисок

try:
    a, b= map(int, input('Введите сколько стоят кг конфет и ирисок').split())
    x, y = map(int, input('Введите сколько кг  конфет и ирисок').split())
    ch = a / x
    cd = b / y
    compar = ch / cd
    print(ch, cd, compar, sep='\n')
except ValueError:
    print('Вы ввели неправильные значения!!!!')


