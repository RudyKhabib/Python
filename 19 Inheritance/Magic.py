class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Sand):
            return Glass()
        else:
            return None

    def info(self):
        print('Огонь')


class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()
        else:
            return None

    def info(self):
        print('Земля')


class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Air):
            return Steam()
        elif isinstance(other, Sand):
            return Clay()
        else:
            return None

    def info(self):
        print('Вода')


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Sand):
            return Sandstorm()
        else:
            return None

    def info(self):
        print('Воздух')


class Storm:
    def info(self):
        print('Шторм')


class Steam:
    def info(self):
        print('Пар')


class Dirt:
    def info(self):
        print('Грязь')


class Lightning:
    def info(self):
        print('Молния')


class Dust:
    def info(self):
        print('Пыль')


class Lava:
    def info(self):
        print('Лава')


class Sand:
    def __add__(self, other):
        if isinstance(other, Water):
            return Clay()
        elif isinstance(other, Air):
            return Sandstorm()
        elif isinstance(other, Fire):
            return Glass()
        else:
            return None

    def info(self):
        print('Песок')


class Clay:
    def info(self):
        print('Глина')


class Glass:
    def info(self):
        print('Стекло')


class Sandstorm:
    def info(self):
        print('Песчаная буря')

