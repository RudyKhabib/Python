import random


class Human:
    def __init__(self, name, house, satiety=50):
        self.name = name
        self.house = house
        self.satiety = satiety
        self.life = True

    def eat(self):
        self.satiety += 10
        self.house.food -= 5

    def work(self):
        self.satiety -= 10
        self.house.money += 20
        if self.satiety < 10:
            self.life = False

    def market(self):
        self.house.food += 20
        self.house.money -= 10

    def play(self):
        self.satiety -= 10
        if self.satiety < 0:
            self.life = False

    def info(self):
        print(self.name)
        if self.life:
            print('Живой')
            print('Денег', self.house.money)
            print('Сытость', self.satiety)
            print('Еды', self.house.food)

        else:
            print('Умер(')


def routine(human):
    fate = random.randint(1, 6)
    if human.satiety < 20:
        human.eat()
    elif human.house.food < 10:
        human.market()
    elif human.house.money < 50:
        human.work()
    elif fate == 1:
        human.work()
    elif fate == 2:
        human.eat()
    else:
        human.play()
