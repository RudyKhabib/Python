people = int(input('Кол-во человек: '))
k_number = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', k_number, 'человек')
lst_ppl = [i + 1 for i in range(people)]
que = 0
print()
for _ in range(people - 1):
    print('Текущий круг людей:', lst_ppl)
    print('Начало счёта с номера', lst_ppl[que])
    if (que + k_number) % len(lst_ppl) == 0:
        loser = lst_ppl.pop()
        que = 0
    else:
        loser = lst_ppl.pop((que + k_number) % len(lst_ppl) - 1)
        que = loser - 1
    print('Выбывает человек под номером', loser)
    print()
print('Остался человек под номером', lst_ppl[0])
