probeg = input('Введите пробег: ')
day = int(input('Введите сегодняшнее число: '))
pr = int(probeg[0])
ob = int(probeg[1])
eg = int(probeg[2])
if pr + ob + eg >= day:
    print('Сброс.')
    probeg = 0
else:
    print('Сегодня не сломался.')
    probeg = int(probeg)
print(probeg)