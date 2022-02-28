numb = int(input('Число: '))
counter = 0
while numb != 0:
    if numb % 2 == 0:
        counter += 1
    numb = int(input('Число: '))
print('Число чётных =', counter)
