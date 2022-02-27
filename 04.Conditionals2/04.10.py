time = int(input('Введите время в часах: '))
if 8 <= time < 10 or 12 <= time < 14 or 15 <= time < 18 or 20 <= time < 22:
    print('Можно получить посылку(1 способ)')
else:
    print('Посылку получить нельзя(1 способ)')
if 22 <= time or time < 8 or 10 <= time < 12 or 14 <= time < 15 or 18 <= time < 20:
    print('Посылку получить нельзя(2 способ)')
else:
    print('Можно получить посылку(2 способ)')
