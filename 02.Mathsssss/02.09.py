''' a = int(input('Введите число: '))
a4 = a // 10
b4 = a % 10
a3 = a4 // 10
b3 = a4 % 10
a2 = a3 // 10
b2 = a3 % 10
a1 = a2 // 10
b1 = a2 % 10
b1 = str(b1)
b2 = str(b2)
b3 = str(b3)
b4 = str(b4)
b = b4 + b3 + b2 + b1
print(int(b)) '''
a = input('Введите число: ')
b = int(a[::-1])
print(b)
