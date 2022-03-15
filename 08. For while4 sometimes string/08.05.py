n = 15
m = 20
i = 8
j = 10
for _ in range(20):
    print('Марсоход находится на позиции', i, ',', j, end=', ')
    direction = input('введите команду: ')
    if direction == 'W' and j < m:
        j += 1
    elif direction == 'S' and j > 0:
        j -= 1
    elif direction == 'D' and i < n:
        i += 1
    elif direction == 'A' and i > 0:
        i -= 1
    for k in range(m, -1 , -1):
        for p in range(n+1):
            if j == k and i == p:
                print('*', end='')
            else:
                print('-', end='')
        print()
print('Хватит на сегодня игрушек')
