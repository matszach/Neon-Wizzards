import pygame
import sys

import src.controllers.views.viewinfo as vi

# fixme todo remove ?
# performance config
# pygame.event.set_allowed([QUIT, KEYDOWN, KEYUP])
flags = [pygame.RESIZABLE | pygame.DOUBLEBUF]
# screen.set_alpha(None)


# those might be moved somewhere else in the future
def set_windowed_mode():
    flags[0] = pygame.RESIZABLE | pygame.DOUBLEBUF
    surface[0] = pygame.display.set_mode((0, 0), flags[0])


def set_full_screen_mode():
    flags[0] = pygame.FULLSCREEN | pygame.DOUBLEBUF
    surface[0] = pygame.display.set_mode((0, 0), flags[0])


# main game surface
surface = [pygame.display.set_mode(
    (vi.window_size_in_units[0]*vi.unit_size[0],
     vi.window_size_in_units[1]*vi.unit_size[0]),
    flags[0])]

# those have to be imported after pygame,display is initialized, because their import prompts imginfo import, which
# requires pygame.display to be already initiated

import src.controllers.entity_handlers as eh
import src.controllers.tile_handlers as th
import src.controllers.gui_handlers as gh


# set app name
pygame.display.set_caption('Neon Wizards')

# manages tme between screen updates
clock = pygame.time.Clock()

# ==================================================== TEST
# fixme #
# this will, in the future, be called withing the main game loop, on button click etc.
from src.game_data.complete_sets.complete_player_characters.estera.pc_estera import PlayerCharacterEstera
from src.controllers.launchers.level_launcher import launch_level
launch_level(PlayerCharacterEstera(), 1, 1)
# ==================================================== TEST

# main game loop
while True:

    clock.tick(60)  # 60 fps
    # a higher value than 60 can be passed also (may be useful to overcome natural fps drop later)

    # print(clock.get_fps())  # move display to game screen

    # list of events (keyboard / mouse presses)
    for event in pygame.event.get():

        # if QUIT (X pressed) -> close the app
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.VIDEORESIZE:
            vi.adjust(event.w, event.h)
            surface[0] = pygame.display.set_mode((event.w, event.h), flags[0])

    # "clears" the screen by filling it with background color
    surface[0].fill((30, 30, 30))

    # handles all active tiles
    th.handle_all(surface[0])

    # handles all active entities
    eh.handle_all(surface[0])

    # handles all gui components
    gh.handle_all(surface[0])

    # draws usable window space
    # vi.draw_usable(surface[0])

    # draws current game state on display
    pygame.display.update()



