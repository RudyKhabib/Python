violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
quantity = int(input('Сколько песен выбрать? '))
counter = 0
for i in range(quantity):
    print('Название', (i + 1), 'песни:', end='')
    song = input()
    j = 0
    while song != violator_songs[j][0]:
        j += 1
    counter += violator_songs[j][1]
print('Общее время звучания песен:', round(counter, 2), 'минут')
