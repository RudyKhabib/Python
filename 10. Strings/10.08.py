numb_n = int(input('Кол-во палок: '))
numb_k = int(input('Кол-во бросков: '))
sticks = ['|' for _ in range(numb_n)]
for j in range(numb_k):
    print('Бросок', j + 1, end='.')
    l_i = int(input('Сбиты палки с номера '))
    r_i = int(input('по номер '))
    for i in range(l_i - 1, r_i):
        sticks[i] = '.'
[print(sticks[i], end='') for i in range(numb_n)]
