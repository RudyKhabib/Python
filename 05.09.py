riddle = int(input('Загадайте число: '))
numb = int(input('Введите число: '))
counter = 1
while numb != riddle:
    counter += 1
    if numb < riddle:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    else:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    numb = int(input('Введите число: '))
print('Вы угадали! Число попыток:', counter)

