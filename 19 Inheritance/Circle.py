from math import pi


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def square(self):
        return pi * (self.r ** 2)

    def perimeter(self):
        return 2 * pi * self.r

    def increase(self, k=1):
        self.r *= k

    def intersection(self, circle2):
        if ((self.x - circle2.x) ** 2 + (self.y - circle2.y) ** 2) ** 1/2 <= (self.r + circle2.r):
            print('Пересекаются')
        else:
            print('Не пересекаются')
