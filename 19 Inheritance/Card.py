import copy
import random


class Card:
    lst_crds_stat = ['2 hearts', '2 clover', '2 pikes', '2 tiles', '3 hearts', '3 clover', '3 pikes', '3 tiles',
                     '4 hearts', '4 clover', '4 pikes', '4 tiles', '5 hearts', '5 clover', '5 pikes', '5 tiles',
                     '6 hearts', '6 clover', '6 pikes', '6 tiles', '7 hearts', '7 clover', '7 pikes', '7 tiles',
                     '8 hearts', '8 clover', '8 pikes', '8 tiles', '9 hearts', '9 clover', '9 pikes', '9 tiles',
                     '10 hearts', '10 clover', '10 pikes', '10 tiles',
                     'Jack hearts', 'Jack clover', 'Jack pikes', 'Jack tiles',
                     'Queen hearts', 'Queen clover', 'Queen pikes', 'Queen tiles',
                     'King hearts', 'King clover', 'King pikes', 'King tiles',
                     'Ace hearts', 'Ace clover', 'Ace pikes', 'Ace tiles', ]
    list_of_cards = copy.deepcopy(lst_crds_stat)
    numbers = '2345678910'

    def __init__(self):
        self.card = random.choice(Card.list_of_cards)
        Card.list_of_cards.pop(Card.list_of_cards.index(self.card))

    def info(self):
        return self.card

    def count(self, summ=0):
        if self.card.split()[0] in Card.numbers:
            return int(self.card.split()[0])
        elif self.card.split()[0] == 'Ace':
            if summ <= 10:
                return 11
            else:
                return 1
        else:
            return 10

    # def __del__(self):
    #     list_of_cards = copy.deepcopy(list_of_cards_static)
