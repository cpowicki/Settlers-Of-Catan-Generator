class edge:

    def __init__(self, v1, v2):
        self.vertex = v1
        self.vertex = v2
        self.is_road = false


class tile:

    def __init__(self, r, n, c):
        self.type = r
        self.number = n
        self.color = c

    def toString(self):
        return ("{} " + self.type).format(self.number)

    def getLabel(self):
        if self.type == 'Desert':
            return 'D'
        else:
            return str(self.number)

    def set_coord(self, coord):
        self.coord = [coord, (coord[0] + 50, coord[1] - 25),
                      (coord[0] + 100, coord[1]), (coord[0] + 100, coord[1] + 50),
                      (coord[0] + 50, coord[1] + 75), (coord[0], coord[1] + 50)]


class vertex:

    def __init__(self, tiles, coord):
        self.vertices = []
        self.tiles = tiles
        self.developments = None
        self.buildable = True
        self.port = []
        self.coord = coord

    def farm(self, roll):
        resources = {}
        yield_num = 0

        if self.developments == None:
            return resources
        elif self.developments == 'Settlement':
            yield_num = 1
        else:
            yield_num = 2

        for i in self.tiles:
            if i.number == roll:
                if i.type in resources.keys():
                    resources[i.type] += yield_num
                else:
                    resources[i.type] = yield_num
        return resources
