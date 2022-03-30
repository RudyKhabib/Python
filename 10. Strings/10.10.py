txt = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
new_txt = ''
for symbol in txt:
    if symbol in alphabet:
        new_txt.format(alphabet[(alphabet.find(symbol) + shift) % len(alphabet)])
    else:
        new_txt.format(symbol)
print('Зашифрованное сообщение:', new_txt)

