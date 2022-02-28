print('Начался 8-часовой рабочий день')
wife = 0
sum = 0
for i in range(1, 9):
    print(str(i) + '-й час')
    hour = int(input('Сколько задач решит Максим? '))
    sum += hour
    mife = int(input('Звонит жена. Взять трубку?(1 - да,0 - нет): '))
    if mife == 1:
        wife += 1
print('Рабочий день закончился.всего выполнено задач:', sum)
if wife > 0:
    print('Нужно в зайти в магазин.')