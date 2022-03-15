x = int(input('Введите число: '))
numerator = 1
for i in range(1, 64, 2):
    numerator *= x-i
denominator = 1
for i in range(0, 65, 2):
    if i != x:
        denominator *= (x-i)
    else:
        denominator *= 1
res = numerator / denominator
print(res)
