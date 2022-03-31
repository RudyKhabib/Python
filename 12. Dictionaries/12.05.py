txt = input('Введите текст:')
lst_txt_new = []
lst_invert = []
dct_txt = dict()
for symbol in txt:
    if symbol not in lst_txt_new:
        lst_txt_new.append(symbol)
        dct_txt[symbol] = txt.count(symbol)
print('Оригинальный словарь частот: ')
[print(key, ':', value) for key, value in dct_txt.items()]
for value in dct_txt.values():
    if value not in lst_invert:
        lst_invert.append(value)
print()
print('Инвентированный словарь частот:')
for numb in lst_invert:
    lst_local = []
    for key, value in dct_txt.items():
        if numb == value:
            lst_local.append(key)
    print(numb, ':', lst_local)
    lst_local.clear()
