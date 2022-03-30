import random
lst1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
lst2 = [round(random.uniform(5, 10), 2) for _ in range(20)]
lst_champ = [lst1[i] if lst1[i] > lst2[i] else lst2[i] for i in range(20)]
print('Первая команда:', lst1)
print('Вторая команда:', lst2)
print('Победители тура:', lst_champ)
