caramba = 'карамба'
counter = 0
words = [i for i in input('Введите слова: ').split()]
for word in words:
    if word == caramba:
        counter += 1
print(counter)

