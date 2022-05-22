class Parent:
    def __init__(self, name, age, children):
        self.name = name
        if age >= max([i.age for i in children]) + 16:
            self.age = age
        else:
            print('Ребенок должен быть младше родителя минимум на 16 лет')
        self.children = children

    def info(self):
        print(f'{self.name}, {self.age} лет')

    def calm(self, i):
        self.children[i].calmness = 'Спокойный'
        print(f'{self.children[i].name} успокоен')

    def feed(self, i):
        self.children[i].hunger = 'Не голодный'
        print(f'{self.children[i].name} накормлен')


class Child:
    def __init__(self, name, age, calmness='Спокойный', hunger='Не голодный'):
        self.name = name
        self.age = age
        self.calmness = calmness
        self.hunger = hunger

    def info(self):
        print(f'{self.name}, {self.calmness}, {self.hunger}')