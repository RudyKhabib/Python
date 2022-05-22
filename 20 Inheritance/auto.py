import math


class Auto:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def move(self, distance):
        self.x = self.x + distance * math.cos(math.pi * self.angle / 180)
        self.y = self.y + distance * math.sin(math.pi * self.angle / 180)

    def turn(self, turn_angle):
        self.angle += turn_angle


class Bus(Auto):
    def __init__(self, x, y, angle, passanger=0, money=0):
        super().__init__(x, y, angle)
        self.passanger = passanger
        self.money = money

    def exit(self, pas):
        self.passanger -= pas
        if self.passanger < 0:
            raise ValueError('Пассажиров не может быть меньше нуля')

    def enter(self, pas):
        self.passanger += pas

    def move(self, distance):
        super().move(distance)
        self.money += self.passanger * distance / 10
