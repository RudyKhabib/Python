paper = float(input('Введите сторону листа: '))
convert = 12
counter = 0
while paper > convert:
    paper /= 2
    counter += 2
print(counter)
