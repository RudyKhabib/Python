square = int(input('Введите площадь квартиры: '))
cost = float(input('Введите стоимость квартиры в миллионах: '))
if square >= 80 and cost <= 7 or square >= 100 and cost <= 10:
    print('Подходит')
else:
    print('Не подходит')