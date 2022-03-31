import copy

n_max = int(input('Введите максимальное число: '))
lst_artem = [i + 1 for i in range(n_max)]
boris = ''
while boris != 'Помогите!':
    print('Нужное число есть среди вот этих чисел: ', end='')
    boris = input()
    if boris != 'Помогите!':
        lst_boris = [int(i) for i in boris.split()]
        artem = input('Ответ Артёма: ')
        if artem.lower() == 'да':
            lst_artem = copy.deepcopy(lst_boris)
        else:
            [lst_artem.pop(lst_artem.index(i)) if i in lst_artem else lst_artem.sort() for i in lst_boris]
print('Артём мог загадать следующие числа: ', end='')
[print(numb, end=' ') for numb in lst_artem]
