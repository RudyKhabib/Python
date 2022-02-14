product1 = int(input('Введите стоимость первого товара: '))
product2 = int(input('Введите стоимость второго товара: '))
product3 = int(input('Введите стоимость третьего товара: '))
amount = product1 + product2 + product3
if amount >= 10000:
    amount = amount * 0.9
print(amount)
