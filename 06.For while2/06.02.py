clients = [int(i) for i in input('Введите 10 чисел: ').split()]
honest = 0
for i in range(len(clients)):
    if clients[i] % 2 == 0 and clients[i] > 0:
        honest += 1
print(honest)
