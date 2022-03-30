text = input('Введите текст: ')
lst_vowels = ['a', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я']
lst_txt_vowels = []
for symbol in text.lower():
    if symbol in lst_vowels:
        lst_txt_vowels.append(symbol)
print('Список гласных букв:', lst_txt_vowels)
print('Длина списка:', len(lst_txt_vowels))
