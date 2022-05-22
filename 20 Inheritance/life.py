class Life:
    def __init__(self, bud):
        self.bud = bud

    def all_life(self):
        with open('karma.log', 'w') as ouf:
            pass
        while self.bud.karma < 500:
            self.bud.one_day()
