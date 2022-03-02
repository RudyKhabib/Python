salary = [int(i) for i in input('Введите числа: ').split()]
check = True
for i in range(len(salary) - 1):
    if salary[i + 1] < salary[i]:
        check = False
if check:
    print('Ваша зарплата растёт')
else:
    print('Ваша зарплата не растёт(')