import numpy as np
from src.controllers.views.painter import paint_tile
import src.controllers.entity_handlers as eh
from math import ceil, floor


"""
tile id = (x, y, tl, tr, br, bl)
x - column of a tile in a tile set
y - row of a tile in a tile set
tl, tr, br, bl - corner block markers True/False
"""
tileIDs = np.zeros((100, 100), dtype=tuple)


def reset():
    pass


def handle_all(surface):

    # here: get player's location and only paint visible tiles
    x_min = eh.PLAYER[0].x - 9
    x_min = floor(x_min) if x_min >= 0 else 0

    x_max = eh.PLAYER[0].x + 9
    x_max = ceil(x_max) if x_max <= len(tileIDs) - 1 else len(tileIDs) - 1

    y_min = eh.PLAYER[0].y - 5
    y_min = floor(y_min) if y_min >= 0 else 0

    y_max = eh.PLAYER[0].y + 5
    y_max = ceil(y_max) if y_max <= len(tileIDs[0]) - 1 else len(tileIDs[0]) - 1

    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            paint_tile(surface, x, y, tileIDs[x][y])

