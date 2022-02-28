riddle = int(input('Загадайте число от 1 до 100: '))
number = 50
maximum = 101
minimum = 0
print('Число', number, '?')
answer = int(input('Введите число(Правильное число : 1, Загаданное больше : 0, Загаданное меньше -1): '))
counter = 0
while answer != 1:
    counter += 1
    if answer != 0:
        maximum = number
        number = number - (number - minimum) // 2
    else:
        minimum = number
        number = (maximum + number) // 2
    print('Число', number, '?')
    answer = int(input('Введите число(Правильное число : 0, Загаданное больше : 0, Загаданное меньше -1): '))
print('Ваше число', number)
print(counter, 'попыток')
