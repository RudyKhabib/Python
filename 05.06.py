marks = int(input('Поставьте оценку: '))
plus = 0
minus = 0
while marks != 0:
    if marks > 0:
        plus += 1
    else:
        minus += 1
    marks = int(input('Поставьте оценку: '))
print('Количество положительных чисел:', plus)
print('Количество отрицательных чисел:', minus)