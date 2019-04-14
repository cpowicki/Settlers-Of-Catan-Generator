import sqlite3
import devcards as d
import time as t

from random import shuffle
from visualize import visualizer
from graph import vertex, tile


x = 300
y = 200


class board:

    # Tiles: 4 Wood, 4 Sheep, 4 Wheat, 3 Brick, 3 Ore

    def __init__(self):
        self.make_tiles()
        self.devdeck = d.deck()

    def make_tiles(self):
        self.numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        shuffle(self.numbers)

        self.tiles = []
        self.board_map = {i: [] for i in self.numbers}

        for i in range(3):

            x = tile("Wood", self.numbers[0], '#006600')
            self.tiles.append(x)
            self.board_map[self.numbers[0]].append(x)
            self.numbers = self.numbers[1:]

            x = tile("Sheep", self.numbers[0], '#99ff33')
            self.tiles.append(x)
            self.board_map[self.numbers[0]].append(x)
            self.numbers = self.numbers[1:]

            x = tile("Wheat", self.numbers[0], '#cccc00')
            self.tiles.append(x)
            self.board_map[self.numbers[0]].append(x)
            self.numbers = self.numbers[1:]

            x = tile("Brick", self.numbers[0], '#cc6600')
            self.tiles.append(x)
            self.board_map[self.numbers[0]].append(x)
            self.numbers = self.numbers[1:]

            x = tile("Ore", self.numbers[0], '#737373')
            self.tiles.append(x)
            self.board_map[self.numbers[0]].append(x)
            self.numbers = self.numbers[1:]

        x = tile("Wood", self.numbers[0], '#006600')
        self.tiles.append(x)
        self.board_map[self.numbers[0]].append(x)
        self.numbers = self.numbers[1:]

        x = tile("Sheep", self.numbers[0], '#99ff33')
        self.tiles.append(x)
        self.board_map[self.numbers[0]].append(x)
        self.numbers = self.numbers[1:]

        x = tile("Wheat", self.numbers[0], '#cccc00')
        self.tiles.append(x)
        self.board_map[self.numbers[0]].append(x)
        self.numbers = self.numbers[1:]

        self.tiles.append(tile("Desert", 0, '#999966'))

        shuffle(self.tiles)


board = board()
view = visualizer()
board = view.visualize_board(board, x, y)

# view.draw_settlement(board.vertices[0].coord, '#ff0000')
# view.draw_road(board.vertices[0].coord, board.vertices[1].coord, '#ff0000')
