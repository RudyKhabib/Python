a, b = input('Введите отрезок: ').split()
a = int(a)
b = int(b)
counter = 0
numbs = 0
for i in range(a,b+1):
    if i % 3 == 0:
        counter += 1
        numbs += i
print(numbs / counter)