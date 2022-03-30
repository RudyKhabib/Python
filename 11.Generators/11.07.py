ip = input('Введите IP: ')
lst_ip = ip.split('.')
is_alpha = False
alpha = 0
small = False
small_one = 0
big = False
big_one = 0
for numb in lst_ip:
    if not numb.isdigit():
        is_alpha = True
        alpha = numb
    elif int(numb) < 0:
        small = True
        small_one = numb
    elif int(numb) > 255:
        big = True
        big_one = numb
if ip.count('.') != 3:
    print('Адрес - это четыре числа, разделённые точками')
elif is_alpha:
    print(alpha, '- не целое число')
elif big:
    print(big_one, 'превышает 255')
elif small:
    print(small_one, 'меньше 0')
else:
    print('IP-адрес корректен')
