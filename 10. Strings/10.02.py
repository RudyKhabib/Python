numb_n = int(input('Введите длину списка: '))
lst_some = [1 if i % 2 == 0 else i % 5 for i in range(numb_n)]
print('Результат', lst_some)