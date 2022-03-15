a = int(input('Введите а: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
j = a
counter = 0
amount = 0
while j % c != 0 and j <= b:
    j += 1
for i in range(j, b+1, c):
    amount += i
    counter += 1
if amount == 0:
    print(amount)
else:
    print(amount / counter)
