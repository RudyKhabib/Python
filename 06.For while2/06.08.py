numb = [int(i) for i in input('Введите числа: ').split()]
for i in range(len(numb)):
    if numb[i] // 100 == 0:
        second_symbol = numb[i] % 10
        first_symbol = numb[i] // 10
        if second_symbol * first_symbol * 3 == numb[i]:
            print(numb[i])

