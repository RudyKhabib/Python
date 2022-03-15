stalls = input('Введите строку: ')
liters = 0
for i in range(len(stalls)):
    if stalls[i] == 'b':
        liters += 2 * (i + 1)
print(liters)