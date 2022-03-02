employee = [float(i) for i in input('СКОЛЬКО ТЫ ЗАРАБАТЫВАЕШЬ ЗА МЕСЯЦ? ').split()]
average = 0
for i in range(12):
    average += employee[i]
average = average / 12
print(average)
# 10 20 10 20 10 20 10 20 10 20 10 20
# 1  2  3  4  5  6  7  8  9  10 11 12
