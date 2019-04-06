from random import shuffle


class developmentCard:

    def __init__(self, type):
        self.type = type


class deck:

    def __init__(self):
        self.cards = []
        for i in range(19):
            self.cards.append(developmentCard('Knight'))

        for i in range(5):
            self.cards.append(developmentCard('Victory Point'))

        for i in range(2):
            self.cards.append(developmentCard('Year of Plenty'))
            self.cards.append(developmentCard('Monopoly'))
            self.cards.append(developmentCard('Road Builder'))
        shuffle(self.cards)
