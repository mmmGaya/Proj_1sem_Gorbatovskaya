st = {}
a = 'Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4'
info = a.split()
key = ['Фамилия', 'Имя', 'Группа', 'Оценки']
for i in range(len(key)):
  st[key[i]] = info[i]

st['Оценки'] = []
for i in info[3:]:
  st['Оценки'].append(int(i))



print(st, sum(st['Оценки'])/len(st['Оценки']), sep='\n')
