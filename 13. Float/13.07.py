flt_xconb, flt_yconb = input('Введите местоположение коня: ').split()
flt_xconb, flt_yconb = float(flt_xconb), float(flt_yconb)
int_xconb, int_yconb = int(10 * flt_xconb), int(10 * flt_yconb)
flt_xpoint, flt_ypoint = input('Введите местоположение точки на доске: ').split()
flt_xpoint, flt_ypoint = float(flt_xpoint), float(flt_ypoint)
int_xpoint, int_ypoint = int(10 * flt_xpoint), int(10 * flt_ypoint)
str_xconb, str_yconb = str(int_xconb), str(int_yconb)
str_xpoint, str_ypoint = str(int_xpoint), str(int_ypoint)
print(f'Конь в клетке ({str_xconb},{str_yconb}). Точка в клетке ({str_xpoint},{str_ypoint})')
if abs((int_xconb - int_xpoint) ** 2 + (int_yconb - int_ypoint) ** 2) == 5:
    print('Да, конь может ходить в эту точку.')

