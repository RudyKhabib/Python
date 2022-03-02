pupil = [int(i) for i in input('Введите оценки учеников: ').split()]
three = 0
four = 0
five = 0
for i in range(len(pupil)):
    if pupil[i] == 3:
        three += 1
    elif pupil[i] == 4:
        four += 1
    else:
        five += 1
print('Отличников:', five, '\n' + 'Хорошистов:', four, '\n' + 'Троечников:', three)