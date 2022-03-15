txt = input('Введите строку: ')
s = 's'
counter = 0
maximum = 0
for ltr in txt:
    if ltr == s:
        counter += 1
        if counter > maximum:
            maximum = counter
    else:
        counter = 0
print('s' * maximum + ',', maximum, 'штук')