from util.gui_elements.decorator import Decorator
from src.controllers.views.imginfo import ABILITY_AND_BAR_GUI
from src.controllers.views.viewinfo import unit_size
from src.controllers.views.viewinfo import current_usable_window_space as cws
from src.controllers import entity_handlers as eh
import pygame


HP_BAR_COLOR = (255, 0, 0)
MP_BAR_COLOR = (0, 0, 255)


class AbilityAndBarGui(Decorator):

    def draw_self(self, surface):

        # parent's draw method. draws the base of the gui
        u = unit_size[0]
        x_off = cws[0]
        y_off = cws[1]

        x = self.x * u + x_off
        y = self.y * u + y_off
        w = self.width * u
        h = self.height * u

        scale_x = round(w)
        scale_y = round(h)

        sprite = pygame.transform.scale(self.img, (scale_x, scale_y))

        surface.blit(sprite, (x, y, w, h))

        # mp and hp bars
        player = eh.PLAYER[0]
        max_bar_width = 106/32 * u
        bar_height = 9/32 * u

        hp_bar_width = player.curr_hp/player.max_hp * max_bar_width
        hp_bar_width = hp_bar_width if hp_bar_width > 0 else 0
        pygame.draw.rect(surface, HP_BAR_COLOR, (x+3/32*u, y+3/32*u, hp_bar_width, bar_height))

        mp_bar_width = player.curr_mp/player.max_mp * max_bar_width
        mp_bar_width = mp_bar_width if mp_bar_width > 0 else 0
        pygame.draw.rect(surface, MP_BAR_COLOR, (x+111/32*u, y+3/32*u, mp_bar_width, bar_height))






    # constructor
    def __init__(self):

        # super constructor
        Decorator.__init__(self, img=ABILITY_AND_BAR_GUI, x=4.5, y=8, width=7, height=1)
