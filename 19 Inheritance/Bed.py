class Bed:
    def __init__(self, lst_potatoes):
        self.lst_potatoes = lst_potatoes

    def growth(self):
        [potato.growth() for potato in self.lst_potatoes]

    def info(self):
        for i in range(len(self.lst_potatoes)):
            print(i, 'ая картошка', end=' ')
            self.lst_potatoes[i].info()
        print()
