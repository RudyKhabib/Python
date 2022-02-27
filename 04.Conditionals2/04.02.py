numb1 = int(input('Введите число: '))
numb2 = int(input('Введите число: '))
numb3 = int(input('Введите число: '))
# 1 способ
print(max(numb1, numb2, numb3, 5))
# 2 способ
if numb3 >= numb1 and numb3 >= numb2:
    print(numb3)
elif numb2 >= numb1 and numb2 >= numb3:
    print(numb2)
else:
    print(numb1)
