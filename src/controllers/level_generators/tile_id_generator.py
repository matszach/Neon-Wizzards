import src.controllers.states.levelinfo as li
import src.controllers.tile_handlers as th
import numpy as np
from random import randint

TILE_DICT = {

    # top, right, bottom, left : x, y
    (False, False, False, False): (0, 0),

    (True, True, True, True): (1, 0),

    (True, False, True, False): (2, 0),
    (False, True, False, True): (3, 0),

    (True, False, False, False): (0, 1),
    (False, True, False, False): (1, 1),
    (False, False, True, False): (2, 1),
    (False, False, False, True): (3, 1),

    (True, False, False, True): (0, 2),
    (True, True, False, False): (1, 2),
    (False, True, True, False): (3, 2),
    (False, False, True, True): (2, 2),

    (True, True, False, True): (0, 3),
    (True, True, True, False): (1, 3),
    (False, True, True, True): (2, 3),
    (True, False, True, True): (3, 3)
}


def translate_to_tile_ids():

    x_len = (len(li.level_fields))
    y_len = (len(li.level_fields[0]))

    th.tileIDs = np.zeros((x_len, y_len), dtype=tuple)

    for x in range(x_len):
        for y in range(y_len):

                tile_type = li.level_fields[x][y]

                # floor -> gets random default floor
                if tile_type == 0:
                    tx = randint(0, 3)
                    ty = randint(5, 6)
                    th.tileIDs[x][y] = (tx, ty, False, False, False, False)

                # wall -> read nearby tiles
                elif tile_type == 1:

                    # check for either map border or for adjacent field
                    top = y < 0 or li.level_fields[x][y-1] == 1
                    right = x >= x_len - 1 or li.level_fields[x+1][y] == 1
                    bottom = y >= y_len - 1 or li.level_fields[x][y+1] == 1
                    left = x < 0 or li.level_fields[x-1][y] == 1

                    tile_x, tile_y = TILE_DICT[(not top, not right, not bottom, not left)]

                    # check for corners (todo fixme)

                    # * top left
                    top_left = top and left and not \
                        (y < 0 or x < 0 or li.level_fields[x-1][y-1] == 1)

                    # * top right
                    top_right = top and right and not \
                        (y < 0 or x >= x_len - 1 or li.level_fields[x+1][y-1] == 1)

                    # * bottom right
                    bottom_right = bottom and right and not \
                        (y >= y_len - 1 or x >= x_len - 1 or li.level_fields[x+1][y+1] == 1)

                    # * bottom left
                    bottom_left = bottom and left and not \
                        (y >= y_len - 1 or x < 0 or li.level_fields[x-1][y+1] == 1)

                    # set correct tileID
                    th.tileIDs[x, y] = (tile_x, tile_y,
                                        top_left, top_right,
                                        bottom_right, bottom_left)

                elif tile_type == 2:
                    pass
                    # todo





