scholarship = int(input('Введите стипендию: '))
payment = int(input('Введите расходы на проживание: '))
credit = 0
for i in range(1, 10+1):
    credit += payment * (1.03 ** (i - 1))
print('У родителей необходимо попросить', round(credit - scholarship * 10, 2))
