numb1 = int(input('Введите первое число: '))
numb2 = int(input('Введите второе число: '))
numb3 = int(input('Введите третье число: '))
if numb1 == numb2 == numb3:
    print(3)
elif numb1 == numb2 or numb1 == numb3 or numb2 == numb3:
    print(2)
else:
    print(0)
