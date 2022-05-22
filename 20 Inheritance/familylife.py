class Life:
    def __init__(self, husband, wife, cat, house):
        self.husband = husband
        self.wife = wife
        self.cat = cat
        self.house = house

    def one_day(self):
        self.house.dirt += 5
        if self.house.dirt > 90:
            self.husband.happiness -= 10
            self.wife.happiness -= 10
        self.husband.activity()
        self.wife.activity()
        self.cat.activity()

    def year(self):
        for _ in range(365):
            self.one_day()
        self.info()

    def info(self):
        if not self.husband.life:
            print('Муж умер', self.husband.nekrolog())
        else:
            print('Муж жив!')
        if not self.wife.life:
            print('Жена умерла', self.wife.nekrolog())
        else:
            print('Жена жива!')
        if not self.cat.life:
            print('Кот умер')
        else:
            print('Кот жив!')
        if self.husband.life and self.wife.life and self.cat.life:
            print('Обалдеть, все живы!!!')
        print(f'Сьедено {self.house.eaten_food} еды')
        print(f'Заработано {self.house.earned_money} деняк')
        print(f'Куплено {self.house.fur_coats} шуб')