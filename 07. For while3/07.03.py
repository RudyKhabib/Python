timer = int(input('Введите время до обнуления таймера: '))
for i in range(timer, -1, -1):
    print('Осталось', i, 'секунд до взрыва')
    answer = int(input('Хотите обезвредить бомбу? '))
    if answer == 1:
        print('Бомба обезврежена за', i, 'секунд до взрыва')
        break
else:
    print('Бомба взорвалась, вы погибли(')
