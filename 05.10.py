riddle = int(input('Загадайте число от 1 до 100'))
number = 50
max = 100
min = 1
print('Число', number, '?')
answer = int(input('Если правильное число, введите 1; Если загаданное число больше, введите 0; Если загаданное число меньше, введите -1'))
while answer !=0:
    if answer == 0:
        min = number
        number = (max - number) // 2
    else:
        max = number
        number = (number - min) // 2
print('вы угадали')
