class Lifo:
    def __init__(self, lst):
        self.lst = lst

    def add(self, element):
        self.lst.append(element)

    def delete(self, elem):
        for _ in range(len(self.lst) - 1, self.lst.index(elem) - 1, -1):
            self.lst.pop()

    def show(self):
        [print(elem, end=' ') for elem in self.lst]
        print()


lifo_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lifo = Lifo(lifo_lst)
lifo.show()
lifo.add(10)
lifo.show()
lifo.delete(3)
lifo.show()
