dict_syn = dict()
numb = int(input('Введите количество пар слов: '))
for i in range(numb):
    print(i + 1, 'пара :', end='')
    lst_local = input().split(' - ')
    dict_syn[lst_local[0]] = lst_local[1]
word = input('Введите слово: ')
check = False
for key, value in dict_syn.items():
    if word.lower() == key.lower():
        print('Синоним:', value)
        check = True
    elif word.lower() == value.lower():
        print('Синоним:', key)
        check = True
if not check:
    print('Такого слова в словаре нет')

