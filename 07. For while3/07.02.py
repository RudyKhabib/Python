debtors = int(input('Введите колиество должников: '))
debt_i = 0
summ = 0
for i in range(0, debtors, 5):
    print('Должник с номером', i)
    debt_i = int(input('Сколько должны? '))
    summ += debt_i
print('Общая сумма долга', summ)
