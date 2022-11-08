# вычисляем сред. ариф и сред. геометрическое от двух чисел
def Mean(x, y):
    al = (x + y)/2
    geo = (x * y)**0.5
    return al, geo
try:
    a, b, c ,d = map(int, input('Введите 4 любых числа: ').split())
    Al_ab, G_ab = Mean(a, b)
    print(f'AB: al - {Al_ab} geo - {round(G_ab, 2)}')
    Al_ac, G_ac = Mean(a, c)
    print(f'AC: al - {Al_ac} geo - {round(G_ac, 2)}')
    Al_ad, G_ad = Mean(a, d)
    print(f'AD: al - {Al_ad} geo - {round(G_ad, 2)}')
except ValueError:
    print('Error:(')