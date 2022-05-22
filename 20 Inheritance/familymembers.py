import random


class Human:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 30
        self.happiness = 30
        self.house = house
        self.life = True

    def eat(self):
        if self.life:
            self.satiety += 30
            self.house.food -= 30
            self.house.eaten_food += 30
            self.life_check()

    def petting(self):
        if self.life:
            self.happiness += 5
            self.satiety -= 10
            self.life_check()

    def life_check(self):
        if self.satiety < 0 or self.happiness < 10:
            self.life = False

    def nekrolog(self):
        if not self.life:
            if self.satiety < 0:
                return 'от голода'
            elif self.happiness < 10:
                return 'от депрессии'


class Husband(Human):
    def __init__(self, name, house):
        super().__init__(name, house)

    def play(self):
        if self.life:
            self.satiety -= 10
            self.happiness += 20
            self.life_check()

    def work(self):
        if self.life:
            self.satiety -= 10
            self.house.money += 1500
            self.house.earned_money += 1500
            self.life_check()

    def activity(self):
        husband_activity = random.randint(1, 2)
        if self.satiety <= 50 and self.house.food >= 10:
            self.eat()
        elif self.house.money <= 50:
            self.work()
        elif husband_activity == 1:
            self.petting()
        else:
            self.play()


class Wife(Human):
    def __init__(self, name, house):
        super().__init__(name, house)

    def grocery(self):
        if self.life:
            self.satiety -= 10
            self.house.food += 10
            self.house.food_cat += 10
            self.house.money -= 20
            self.life_check()

    def fur_coat(self):
        if self.life:
            self.satiety -= 10
            self.house.money -= 350
            self.house.fur_coats += 1
            self.happiness += 60
            self.life_check()

    def clean(self):
        if self.life:
            self.satiety -= 10
            if self.house.dirt > 100:
                self.house.dirt -= 100
            else:
                self.house.dirt = 0
            self.life_check()

    def activity(self):
        wife_activity = random.randint(1, 2)
        if self.satiety <= 50 and self.house.food >= 10:
            self.eat()
        elif (self.house.food <= 20 or self.house.food_cat <= 10) and self.house.money >= 10:
            self.grocery()
        elif self.house.dirt >= 30:
            self.clean()
        elif wife_activity == 1 and self.house.money > 500:
            self.fur_coat()
        else:
            self.petting()


class Cat:
    def __init__(self, name, house):
        self.name = name
        self.satiety = 30
        self.house = house
        self.life = True

    def eat(self):
        if self.life:
            self.satiety += 20
            self.house.food_cat -= 10

    def sleep(self):
        if self.life:
            self.satiety -= 10
            if self.satiety < 0:
                self.life = False

    def wallpaper(self):
        if self.life:
            self.satiety -= 10
            self.house.dirt += 5
            if self.satiety < 0:
                self.life = False

    def activity(self):
        cat_activity = random.randint(1, 2)
        if self.satiety <= 10 < self.house.food_cat:
            self.eat()
        elif cat_activity == 1:
            self.sleep()
        else:
            self.wallpaper()


class House:
    def __init__(self):
        self.money = 100
        self.food = 50
        self.food_cat = 30
        self.dirt = 0
        self.earned_money = 0
        self.fur_coats = 0
        self.eaten_food = 0

    def info(self):
        print(f'Осталось {self.money} деняк')
        print(f'Осталось {self.food} еды')
        print(f'Осталось {self.food_cat} еды для кота')
        print(f'Грязи {self.dirt} ')
