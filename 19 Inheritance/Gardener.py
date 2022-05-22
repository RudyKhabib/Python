class Gardener:
    def __init__(self, name, bed):
        self.name = name
        self.bed = bed

    def care(self):
        self.bed.growth()
        print(f'Садовник {self.name} ухажвивает за грядкой')

    def harvest(self):
        counter = 0
        lst_ripe = list()
        i = 0
        for potato in self.bed.lst_potatoes:
            if potato.state == 3:
                counter += 1
                lst_ripe.append(i)
            i += 1
        [self.bed.lst_potatoes.pop(j) for j in lst_ripe]