scats = int(input('Кол-во коньков: '))
lst_scats = []
for i in range(scats):
    print('Размер', i + 1, 'пары: ', end='')
    lst_scats.append(int(input()))
people = int(input('Кол-во людей: '))
lst_ppl = []
for i in range(people):
    print('Размер ноги', i + 1, 'человека: ', end='')
    lst_ppl.append(int(input()))
lst_ppl.sort()
lst_scats.sort()
lst_ppl = lst_ppl[::-1]
lst_scats = lst_scats[::-1]
i = scats - 1
j = people - 1
counter = 0
while i >= 0 and j >= 0:
    if lst_ppl[j] <= lst_scats[i]:
        i -= 1
        j -= 1
        counter += 1
    else:
        i -= 1
print('Наибольшее кол-во людей, которые могут взять ролики', counter)

