import copy

lst_n = [int(i) for i in input('Введите список: ').split()]
lst_n2 = copy.deepcopy(lst_n)
lst_zeroes = []
counter = 0
for i in range(len(lst_n)):
    if lst_n[i] == 0:
        counter += 1
        lst_zeroes.append(i)
for i in range(len(lst_zeroes) - 1, -1, -1):
    lst_n2.pop(lst_zeroes[i])
[lst_n2.append(0) for _ in range(counter)]
lst_n = copy.deepcopy(lst_n2)
print(lst_n)
[lst_n.pop() for _ in range(counter)]
print(lst_n)

