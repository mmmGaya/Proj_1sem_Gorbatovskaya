
# Ответить на вопросы:
# 1. какие туры из Вояж отсутствуют в РейнТуре
# 2. какие туры из РейнТуре отсутствуют в Вояж
# 3. перечень одинаковых туров
# 4. равны ли перечни туров

voa = {'Мексика', 'Канада', 'Израиль', 'Италия'}
rtyr = {'Англия', 'Япония', 'Канада', 'ЮАР'}

one = voa - rtyr
two = rtyr - voa
three = voa & rtyr
four = voa == rtyr

print(one, two, three, four,  sep='\n')