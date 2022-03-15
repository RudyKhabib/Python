txt = input('Введите текст: ')
space = ' '
counter = 0
maximum = 0
for ltr in txt:
    if ltr == space:
        counter = 0
    else:
        counter += 1
        if counter > maximum:
            maximum = counter
print('Самое длинное слово, букв:', maximum)
