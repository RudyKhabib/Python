class Potato:
    states = {0: 'Отсутствует',
              1: 'Росток',
              2: 'Зеленая',
              3: 'Зрелая'}

    def __init__(self, number, state):
        self.number = number
        self.state = state

    def info(self):
        print(Potato.states[self.state])

    def growth(self):
        if self.state < len(Potato.states) - 1:
            self.state += 1
        else:
            self.state = 0
            # print('Картошка перезрела')