import PIL.ImageDraw as ImageDraw
import PIL.Image as Image
import PIL.ImageColor as ImageColor
import PIL.ImageFont as ImageFont
from graph import vertex
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


class visualizer():

    def __init__(self):
        self.font = ImageFont.truetype("Freshman.ttf", size=30)
        self.image = Image.new("RGB", size=(900, 900), color="#f5f5dc")
        self.draw = ImageDraw.Draw(self.image)

    def add_harbors_standard(self, x_offset, y_offset):
        s = 20
        start = x_offset - s
        y_offset -= 70
        points = ((start, y_offset), (start + 300 + (2 * s), y_offset),
                  (start + 475, y_offset + 245), (start + 300 + (2 * s), y_offset + 475),
                  (start, y_offset + 475), (start - 130, y_offset + 245))

        self.draw.polygon((points), fill="#0066ff", outline="#000000")

    def draw_settlement(self, c, color):
        l = 16
        w = 10
        points = [(c[0]-l, c[1] - w),
                  (c[0], c[1]-20),
                  (c[0]+l, c[1]-w),
                  (c[0]+l, c[1]+w),
                  (c[0]-l, c[1]+w)]

        self.draw.polygon(points, fill=color, outline="#000000")
        plt.imshow(self.image)
        plt.draw()
        plt.pause(0.001)

    def draw_road(self, start, end, color):
        self.draw.line([start, end], fill=color, width=5)
        plt.imshow(self.image)
        plt.draw()
        plt.pause(0.001)

    def add_vertices(self, tiles):
        r = 3
        vert_map = {}
        for i in tiles:
            for c in i.coord:
                if c in vert_map.keys():
                    vert_map[c].tiles.append(i)
                else:
                    vert_map[c] = vertex([i], c)
                box = (c[0]-r, c[1]-r, c[0]+r, c[1]+r)
                self.draw.ellipse(box, fill="#000000")

        return list(vert_map.values())

    def visualize_board(self, board, x_offset, y_offset):

        row1 = board.tiles[:3]
        row2 = board.tiles[3:7]
        row3 = board.tiles[7:12]
        row4 = board.tiles[12:16]
        row5 = board.tiles[16:]

        self.add_harbors_standard(x_offset, y_offset)

        for i in range(3):
            start = x_offset + (100 * i)
            row1[i].set_coord((start, y_offset))
            self.draw.polygon((row1[i].coord), fill=row1[i].color, outline="#000000")
            if row1[i].number > 9:
                self.draw.text((start+35, y_offset + 15), row1[i].getLabel(),
                               fill="#000000", font=self.font)
            else:
                self.draw.text((start+38, y_offset + 15), row1[i].getLabel(),
                               fill="#000000", font=self.font)

        x_offset -= 50
        y_offset += 75

        for i in range(4):
            start = x_offset + (100 * i)
            row2[i].set_coord((start, y_offset))
            self.draw.polygon((row2[i].coord), fill=row2[i].color, outline="#000000")
            if row2[i].number > 9:
                self.draw.text((start+35, y_offset + 15), row2[i].getLabel(),
                               fill="#000000", font=self.font)
            else:
                self.draw.text((start+38, y_offset + 15), row2[i].getLabel(),
                               fill="#000000", font=self.font)

        x_offset -= 50
        y_offset += 75

        for i in range(5):
            start = x_offset + (100 * i)
            row3[i].set_coord((start, y_offset))
            self.draw.polygon((row3[i].coord), fill=row3[i].color, outline="#000000")
            if row3[i].number > 9:
                self.draw.text((start+35, y_offset + 15), row3[i].getLabel(),
                               fill="#000000", font=self.font)
            else:
                self.draw.text((start+38, y_offset + 15), row3[i].getLabel(),
                               fill="#000000", font=self.font)
        x_offset += 50
        y_offset += 75

        for i in range(4):
            start = x_offset + (100 * i)
            row4[i].set_coord((start, y_offset))
            self.draw.polygon((row4[i].coord), fill=row4[i].color, outline="#000000")
            if row4[i].number > 9:
                self.draw.text((start+35, y_offset + 15), row4[i].getLabel(),
                               fill="#000000", font=self.font)
            else:
                self.draw.text((start+38, y_offset + 15), row4[i].getLabel(),
                               fill="#000000", font=self.font)
        x_offset += 50
        y_offset += 75

        for i in range(3):
            start = x_offset + (100 * i)
            row5[i].set_coord((start, y_offset))
            self.draw.polygon((row5[i].coord), fill=row5[i].color, outline="#000000")
            if row5[i].number > 9:
                self.draw.text((start+35, y_offset + 15), row5[i].getLabel(),
                               fill="#000000", font=self.font)
            else:
                self.draw.text((start+38, y_offset + 15), row5[i].getLabel(),
                               fill="#000000", font=self.font)

        board.vertices = self.add_vertices(board.tiles)
        self.gameview = plt.figure(figsize=(8, 6.5))
        plt.imshow(self.image)
        plt.axis('off')
        plt.ion()
        plt.show()
        plt.pause(0.001)
        return board
