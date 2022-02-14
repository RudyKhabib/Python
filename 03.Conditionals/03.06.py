kostya = int(input('Кубик Кости: '))
vlad = int(input('Кубик владельца: '))
if kostya >= vlad:
    print('Разность:', kostya - vlad)
    print('Костя платит')
else:
    print('Сумма:', kostya + vlad)
    print('Владелец платит')
print('Игра окончена')