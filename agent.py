import random


class agent:

    def __init__(self, color):
        self.points = 0
        self.resources = {
            "Brick": 0,
            "Wood": 0,
            "Wheat": 0,
            "Sheep": 0,
            "Ore": 0,
        }
        self.dev_cards = []
        self.vertices = []
        self.color = color

    def get_actions():
        roads = min(self.resources["Brick"], self.resources["Wood"])
        dev_cards = min(self.resources["Wheat"], self.resources["Sheep"], self.resources["Ore"])
        settlement = min(self.resources["Wheat"], self.resources["Sheep"],
                         self.resources["Brick"], self.resources["Wood"])
        city = min(self.resources["Ore"] // 3, self.resources["Wheat"] // 2)

    def pickup(roll):
        for i in self.vertices:
            vert_yield = i.farm(roll)
            for r in vert_yield.keys():
                self.resources[r] += vert_yield[r]

    def turn():
        roll = r.randint(1, 6) + r.randint(1, 6)
        pickup(roll)

    def add_settlement():
        self.points += 1
