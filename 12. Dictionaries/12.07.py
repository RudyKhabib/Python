i_order = int(input('Введите количество заказов: '))
d_order = dict()
for i in range(i_order):
    print(i + 1, 'заказ: ', end='')
    lst_local = input().split(' ')
    if lst_local[0] not in d_order.keys():
        d_order[lst_local[0]] = {lst_local[1]: int(lst_local[2])}
    else:
        if lst_local[1] in d_order[lst_local[0]].keys():
            d_order[lst_local[0]][lst_local[1]] += int(lst_local[2])
        else:
            d_order[lst_local[0]].update({lst_local[1]: lst_local[2]})
    lst_local.clear()
for name, menu in sorted(d_order.items()):
    print(name, ':')
    for pizza, counter in sorted(menu.items()):
        print('\t', pizza, ':', counter, sep='')
