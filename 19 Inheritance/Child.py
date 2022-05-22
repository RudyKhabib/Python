class Child:
    def __init__(self, name, age, calmness='Спокойный', hunger='Не голодный'):
        self.name = name
        self.age = age
        self.calmness = calmness
        self.hunger = hunger

    def info(self):
        print(f'{self.name}, {self.calmness}, {self.hunger}')