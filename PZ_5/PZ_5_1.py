#составить функцию которая печатает сорок любых символов

def print_sumbols():
    try:
        val = int(input('Введите любое число больше 35: '))
        for i in range(40):
            print(chr(i + val), end=' ')
    except ValueError:
        print('Ошибочка')



print_sumbols()