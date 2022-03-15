code = input('Введите зашифрованный сендвич: ')
word = ['a' for i in range(len(code))]
beginning = 0
end = len(code) - 1
for i in range(len(code)):
    if i % 2 == 0:
        word[beginning] = code[i]
        beginning += 1
    else:
        word[end] = code[i]
        end -= 1
print('Расшифрованный сендвич:', ''.join(word))
