name = input('Введите имя: ')
debt = int(input('Введите долг: '))
print(name + ',', 'ваша задолженность составляет', debt, 'рублей.')
money = int(input('Сколько рублей вы внесётё прямо сейчас, чтобы её погасить? '))
while money <= debt:
    print('Маловато,',name + '.', 'Давайте ещё раз.')
    money = int(input('Сколько рублей вы внесётё прямо сейчас, чтобы её погасить? '))
print('Отлично,', name + '!', 'Вы погасили долг. Спасибо!')