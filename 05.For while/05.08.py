X = int(input('Введите начальный вклад: '))
P = int(input('Введите процентную ставку: '))
Y = int(input('Введите конечный вклад: '))
summ = int(X * (1 + P / 100))
year = 1
while summ <= Y:
    summ *= (1 + P / 100)
    summ = int(summ)
    year += 1
print(year)
