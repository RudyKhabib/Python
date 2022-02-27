dudb = int(input('СКОЛЬКО ТЫ ЗАРАБАТЫВАЕШЬ?! '))
if dudb > 50000:
    nalog = 0.3 * (dudb - 50000) + 0.2 * (50000 - 10000) + 0.13 * 10000
elif 10000 < dudb <= 50000:
    nalog = 0.2 * (dudb - 10000) + 0.13 * 10000
else:
    nalog = 0.13 * dudb
print('Плоти налог', nalog)
