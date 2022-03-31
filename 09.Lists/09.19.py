friends = int(input('Кол-во друзей: '))
debts = int(input('Долговых расписок: '))
lst_friends = [0 for i in range(friends)]
for i in range(debts):
    print()
    print(i + 1, 'расписка')
    to_smb = int(input('Кому: '))
    from_smb = int(input('От кого: '))
    how_mch = int(input('Сколько: '))
    lst_friends[to_smb - 1] -= how_mch
    lst_friends[from_smb - 1] += how_mch
print()
print('Баланс друзей:')
[print(i + 1, ':', lst_friends[i]) for i in range(friends)]
