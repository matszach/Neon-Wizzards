from util.gui_elements.decorator import Decorator
from src.controllers.views.imginfo import ABILITY_AND_BAR_GUI
from src.controllers.views.viewinfo import unit_size
from src.controllers.views.viewinfo import current_usable_window_space as cws
from src.controllers import entity_handlers as eh
import pygame
from os import sep as sep


HP_BAR_COLOR = (255, 0, 0)
MP_BAR_COLOR = (0, 0, 255)
ABILITY_CHOSEN_COLOR = (120, 60, 0)
KEY_SYMBOLS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=']


class AbilityAndBarGui(Decorator):

    def draw_self(self, surface):

        # ===== parent's draw method. draws the base of the gui =====
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

        # ===== mp and hp bars =====
        player = eh.PLAYER[0]
        max_bar_width = 106/32 * u
        bar_height = 9/32 * u
        font = pygame.font.Font(f'resources{sep}fonts{sep}menu_font.otf', round(u/4.5))

        # hp
        hp_bar_width = player.curr_hp/player.max_hp * max_bar_width
        hp_bar_width = hp_bar_width if hp_bar_width > 0 else 0
        hp_x = x+3/32*u
        hp_y = y+3/32*u
        pygame.draw.rect(surface, HP_BAR_COLOR, (hp_x, hp_y, hp_bar_width, bar_height))
        hp_txt_surf = font.render(f'{round(player.curr_hp)}/{player.max_hp}', True, (0, 0, 0))
        hp_txt_rect = hp_txt_surf.get_rect()
        hp_txt_rect.center = (hp_x+max_bar_width/2, hp_y+bar_height/2)
        surface.blit(hp_txt_surf, hp_txt_rect)

        # mp
        mp_bar_width = player.curr_mp/player.max_mp * max_bar_width
        mp_bar_width = mp_bar_width if mp_bar_width > 0 else 0
        mp_x = x + 111 / 32 * u
        mp_y = y + 3 / 32 * u
        pygame.draw.rect(surface, MP_BAR_COLOR, (mp_x, mp_y, mp_bar_width, bar_height))
        mp_txt_surf = font.render(f'{round(player.curr_mp)}/{player.max_mp}', True, (0, 0, 0))
        mp_txt_rect = mp_txt_surf.get_rect()
        mp_txt_rect.center = (mp_x + max_bar_width / 2, mp_y + bar_height / 2)
        surface.blit(mp_txt_surf, mp_txt_rect)

        # ===== abilities =====
        border = 2 / 32 * u
        icon_width = round(u / 2)
        y_ab = y + 13 / 32 * u
        x_init = x + 1.5 * border

        # icons
        for i, ability in enumerate(player.abilities):
            sprite = pygame.transform.scale(ability.icon, (icon_width, icon_width))
            surface.blit(sprite, (x_init + i * (icon_width + border), y_ab, icon_width, icon_width))

        # chosen ability
        pygame.draw.rect(surface, ABILITY_CHOSEN_COLOR,
                         (x_init + player.ability_chosen * (icon_width + border), y_ab, icon_width, icon_width), 4)

        # ability keys
        y_ab = y_ab + 13 / 32 * u
        x_init = x_init + 14 / 32 * u
        for i in range(12):
            txt_surf = font.render(f'{KEY_SYMBOLS[i]}', True, (90, 40, 0))
            txt_rect = txt_surf.get_rect()
            txt_rect.center = (x_init + i * (icon_width + border), y_ab)
            surface.blit(txt_surf, txt_rect)

    # constructor
    def __init__(self):

        # super constructor
        Decorator.__init__(self, img=ABILITY_AND_BAR_GUI, x=4.5, y=8, width=7, height=1)

