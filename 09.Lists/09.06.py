some_str = input('Введите строку: ')
# 1 способ
some_set = set(some_str)
print(len(some_set))
# 2 способ
certain_str = []
counter = 0
for sltr in some_str:
    if sltr not in certain_str:
        certain_str.append(sltr)
        counter += 1
print(counter)
