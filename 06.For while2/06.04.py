summ = 0
for i in range(30, 36):
    print('Людей в', str(i) + '-м секторе:', end='')
    intruder = int(input(' '))
    if intruder > 10:
        print('Нарушение! Слишком много людей в секторе!')
        summ += 1
    else:
        print('Всё спокойно.')
print('Количество нарушений:', summ)
