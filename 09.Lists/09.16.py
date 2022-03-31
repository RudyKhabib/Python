print('Введите 3 числа: ')
lst1 = [input() for _ in range(3)]
print('Введите 7 чисел: ')
lst2 = [input() for _ in range(7)]
print(lst1)
print(lst2)
lst1.extend(lst2)
print('Новый первый список с уникальными элементами:', list(set(lst1)))
