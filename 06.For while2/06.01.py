numbs = [int(i) for i in input('Введите шыфр: ').split()]
for i in range(len(numbs)):
    if numbs[i] % 2 == 0 and numbs[i] % 3 != 0:
        print(numbs[i], 'Число подходит')
    else:
        print(numbs[i], 'Число не подходит')
# 114 12 14 10605 4907 450
