import pygame
import sys
import src.controllers.views.viewinfo as vi

flags = [pygame.RESIZABLE | pygame.DOUBLEBUF]

# main game surface
surface = [pygame.display.set_mode(
    (vi.window_size_in_units[0]*vi.unit_size[0],
     vi.window_size_in_units[1]*vi.unit_size[0]),
    flags[0])]

# initiates font, otherwise no text could be displayed
pygame.font.init()

# those have to be imported after pygame,display is initialized, because their import prompts imginfo import, which
# requires pygame.display to be already initiated
from src.controllers.views.imginfo import GAME_ICON
import src.controllers.entity_handlers as eh
import src.controllers.tile_handlers as th
import src.controllers.gui_handlers as gh

# set app name
pygame.display.set_caption('Neon Wizards')
pygame.display.set_icon(GAME_ICON)

# manages tme between screen updates
clock = pygame.time.Clock()

# initial view launcher
from src.controllers.launchers.main_menu_launcher import launch_main_menu
launch_main_menu()

# main game loop
while True:

    clock.tick(60)  # 60 fps
    # a higher value than 60 can be passed also (may be useful to overcome natural fps drop later)

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
    # vi.draw_usable(surface[0])\
    vi.hide_unusable(surface[0])
    # print(clock.get_fps())  # move display to game screen

    # draws current game state on display
    pygame.display.update()

