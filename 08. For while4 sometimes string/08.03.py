txt = input('Введите текст: ')
star = '*'
i = 1
for ltr in txt:
    if ltr == star:
        print('Символ "*" стоит на позиции', i)
    else:
        i += 1