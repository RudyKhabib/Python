x = int(input('Введите количество мужчин: '))
y = int(input('Введите количество девочек: '))
if x > 2 * y or y > 2 * x:
    print('Нет решения ')
elif x > y:
    print('BGB' * (x-y) + 'GB' * (y - (x - y)))
elif x < y:
    print('GBG' * (y - x) + 'BG' * ( x - (y - x)))
else:
    print('GB' * y)
