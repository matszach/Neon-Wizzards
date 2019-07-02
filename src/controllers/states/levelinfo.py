import numpy as np

"""
0 - floor, can be walked over
1 - wall, can't be walked over, blocks projectiles
2 - pit, can't be walked over, doesn't block projectiles
"""

level_fields = np.zeros((100, 100), dtype=int)


def get_field_at(x, y):

    # out of range fields return 1 as for wall
    if x < 0 or y < 0 or x >= len(level_fields) or y >= len(level_fields[0]):
        return 1
    else:
        return level_fields[round(x)][round(y)]

