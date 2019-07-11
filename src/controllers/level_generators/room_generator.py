from math import floor, ceil


def generate_room_plain(x, y, w, h, level_map):
    for ix in range(x - ceil(w/2), x + floor(w/2)):
        for iy in range(y - ceil(h / 2), y + floor(h / 2)):
            level_map[ix][iy] = 0
