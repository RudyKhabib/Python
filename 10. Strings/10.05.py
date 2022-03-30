txt = input('Введите строку: ')
start_h = txt.lower().find('h')
end_h = len(txt) - (txt[::-1].lower().find('h') + 1)
print(txt[end_h:start_h - 1:-1])
