import numpy as np

"""
0 - floor, can be walked over
1 - wall, can't be walked over, blocks projectiles
2 - pit, can't be walked over, doesn't block projectiles
"""

level_fields = np.zeros((100, 100), dtype=int)


def get_field_at(x, y):
    return level_fields[round(x)][round(y)]
