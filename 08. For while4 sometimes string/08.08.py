colontitul = int(input('Введите длину колонтитула: '))
sign = int(input('Введите количество восклицательных знаков: '))
first = colontitul // 2
print('~' * first + '!' * sign + '~' * (colontitul - first))