import pygame
import sys

import src.controllers.views.viewinfo as vi
import src.controllers.entity_handlers as eh
import src.controllers.tile_handlers as th
import src.controllers.gui_handlers as gh

# main game surface
surface = pygame.display.set_mode(
    (vi.window_size_in_units[0]*vi.unit_size[0],
     vi.window_size_in_units[1]*vi.unit_size[0]),
    pygame.RESIZABLE)

# set app name
pygame.display.set_caption('Cool Game')

# manages tme between screen updates
clock = pygame.time.Clock()

# main game loop
while True:

    clock.tick(17)

    # list of events (keyboard / mouse presses)
    for event in pygame.event.get():

        # if QUIT (X pressed) -> close the app
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.VIDEORESIZE:
            vi.adjust(event.w, event.h)
            surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    # "clears" the screen by filling it with background color
    surface.fill((0, 0, 0))

    # handles all active tiles
    th.handle_all()

    # handles all active entities
    eh.handle_all()

    # handles all gui components
    gh.handle_all()

    # draws usable window space
    vi.draw_usable(surface)

    # draws current game state on display
    pygame.display.update()
