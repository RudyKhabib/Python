numb_seq = int(input('Кол-во чисел: '))
lst_seq = []
lst_add = []
seq = False
for _ in range(numb_seq):
    lst_seq.append(int(input('Число: ')))
print('Последовательность: ', end='')
[print(numb, end=' ') for numb in lst_seq]
print()
que = len(lst_seq) / 2
while not seq and que < len(lst_seq):
    if not que.is_integer():
        end = len(lst_seq) - 1 - int(que)
        if lst_seq[int(que) + 1:] == lst_seq[int(que) - 1: int(que) - end - 1: -1]:
            seq = True
            lst_add = lst_seq[int(que) - end - 1::-1]
    else:
        end = len(lst_seq) - que
        if lst_seq[int(que):] == lst_seq[int(que - 1):int(que - end - 1): -1]:
            seq = True
            lst_add = lst_seq[int(que - end - 1):: -1]
    que += 0.5
print('Нужно приписать чисел:', len(lst_add))
print('Сами числа:', end=' ')
[print(i, end=' ') for i in lst_add]
