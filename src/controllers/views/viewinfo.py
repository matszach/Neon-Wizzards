import pygame

window_size_in_units = 16, 9

width_to_height_ratio = 16/9

unit_size = [64]

current_usable_window_space = [0, 0, window_size_in_units[0]*unit_size[0], window_size_in_units[1]*unit_size[0]]


def adjust(win_w, win_h):

    if win_w >= width_to_height_ratio * win_h:
        w = win_h * width_to_height_ratio
        h = win_h
        x = (win_w - w) / 2
        y = 0
    else:
        w = win_w
        h = win_w * 1/width_to_height_ratio
        x = 0
        y = (win_h - h) / 2

    current_usable_window_space[0] = x
    current_usable_window_space[1] = y
    current_usable_window_space[2] = w
    current_usable_window_space[3] = h
    unit_size[0] = w/window_size_in_units[0]

    print(f'LOG: Screen re-sized.'
          f'\n\t Current usable area: (x: {round(x,2)}, y: {round(y,2)}, w: {round(w,2)}, h: {round(h,2)}).'
          f'\n\t Current unit size: {round(unit_size[0],2)}')


def draw_usable(surface):

    for i in range(0, window_size_in_units[0]+1):
        ys = 0 + current_usable_window_space[1]
        ye = current_usable_window_space[3] + current_usable_window_space[1]
        x = i * unit_size[0] + current_usable_window_space[0]
        pygame.draw.line(surface, (70, 70, 70), (x, ys), (x, ye))

    for i in range(0, window_size_in_units[1]+1):
        xs = 0 + current_usable_window_space[0]
        xe = current_usable_window_space[2] + current_usable_window_space[0]
        y = i * unit_size[0] + current_usable_window_space[1]
        pygame.draw.line(surface, (70, 70, 70), (xs, y), (xe, y))
