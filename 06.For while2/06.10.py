N = int(input('Введите число карточек: '))
cards = [int(i) for i in input('Введите карточки: ').split()]
for i in range(1,N+1):
    check = False
    for j in range(N-1):
        if i == cards[j]:
            check = True
    if not check:
        print(i)
        break
