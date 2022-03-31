txt = input('Введите строку:')
d_counter = dict()
is_pol = True
counter_1 = 0
for symbol in txt:
    d_counter[symbol] = txt.count(symbol)
for value in d_counter.values():
    if value == 1 and counter_1 == 0:
        counter_1 = 1
    elif value == 1 and counter_1 > 0:
        is_pol = False
    elif value % 2 != 0:
        is_pol = False
if is_pol:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
