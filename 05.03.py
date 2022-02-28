numb = int(input('Введите число: '))
order = 1
while numb // 10 != 0:
    order += 1
    numb = numb // 10
print(order, 'знаков числа')