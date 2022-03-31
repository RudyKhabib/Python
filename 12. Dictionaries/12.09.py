n_people = int(input('Введите количество человек: '))
d_family = dict()
d_height = dict()
for i in range(n_people - 1):
    print(i + 1, 'пара:', end='')
    child, parent = input().split()
    d_family[child] = parent
for parent in d_family.values():
    if parent not in d_family.keys():
        d_height[parent] = 0
for child in d_family.keys():
        d_height[child] = d_height[d_family[child]] + 1
print('"Высота" каждого члена семьи:')
[print(key, value) for key, value in sorted(d_height.items())]



# Введите количество человек: 9
# 1 пара: Alexei Peter_I
# 2 пара: Anna Peter_I
# 3 пара: Elizabeth Peter_I
# 4 пара: Peter_II Alexei
# 5 пара: Peter_III Anna
# 6 пара: Paul_I Peter_III
# 7 пара: Alexander_I Paul_I
# 8 пара: Nicholaus_I Paul_I
#
# “Высота” каждого члена семьи:
# Alexander_I 4
# Alexei 1
# Anna 1
# Elizabeth 1
# Nicholaus_I 4
# Paul_I 3
# Peter_I 0
# Peter_II 2
# Peter_III 2
