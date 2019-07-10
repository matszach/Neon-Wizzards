from util.gui_elements.gui_element import GuiElement
from src.controllers.views.viewinfo import unit_size
from src.controllers.views.viewinfo import current_usable_window_space as cws
from pygame import mouse
from src.controllers.views.imginfo \
    import MENU_WIDE_BUTTON_OFF, MENU_WIDE_BUTTON_ON, MENU_NARROW_BUTTON_OFF, MENU_NARROW_BUTTON_ON
import pygame
from os import sep as SEP


class Button(GuiElement):

    def listen(self):
        if self.is_mouse_on():
            if self.is_mouse_down():
                self.activated = True
            elif self.activated:
                self.action()
                self.activated = False

    def is_mouse_on(self):
        u = unit_size[0]
        x = cws[0]/u + self.x
        y = cws[1]/u + self.y
        pos_x, pos_y = mouse.get_pos()
        return x < pos_x/u < x + self.width and y < pos_y/u < y + self.height

    @staticmethod
    def is_mouse_down():
        return mouse.get_pressed()[0]

    def draw_self(self, surface):

        u = unit_size[0]
        x_off = cws[0]
        y_off = cws[1]

        x = self.x * u + x_off
        y = self.y * u + y_off
        w = self.width * u
        h = self.height * u

        scale_x = round(w)
        scale_y = round(h)

        if self.is_mouse_on():
            sprite = pygame.transform.scale(self.img_on, (scale_x, scale_y))
            font_size = round(u / 2.8)
        else:
            sprite = pygame.transform.scale(self.img_off, (scale_x, scale_y))
            font_size = round(u / 3.2)

        surface.blit(sprite, (x, y, w, h))

        # render text, centered around the center of the button
        # font load might be replaced / moved
        font = pygame.font.Font(f'resources{SEP}fonts{SEP}menu_font.otf', font_size)
        txt_surf = font.render(self.text, True, (0, 0, 0))
        txt_rect = txt_surf.get_rect()

        # center text rect in the middle of the button
        txt_rect.center = ((x + w / 2), (y + h / 2))
        surface.blit(txt_surf, txt_rect)

    # constructor
    def __init__(self, img_on=MENU_WIDE_BUTTON_ON, img_off=MENU_WIDE_BUTTON_OFF,
                 x=0, y=0, width=4, height=1, text='Button', on_action=lambda: None):

        # super constructor
        GuiElement.__init__(self, x, y)

        # images
        self.img_on = img_on
        self.img_off = img_off

        # button's dimensions
        self.width = width
        self.height = height

        # button's text
        self.text = text

        # button's on-click action
        self.action = on_action

        # marks button as activated
        self.activated = False


class WideButton(Button):

    def __init__(self, x=0, y=0, text='Button', on_action=lambda: None):
        Button.__init__(self, MENU_WIDE_BUTTON_ON, MENU_WIDE_BUTTON_OFF, x, y, 4, 1, text, on_action)


class NarrowButton(Button):

    def __init__(self, x=0, y=0, text='Button', on_action=lambda: None):
        Button.__init__(self, MENU_NARROW_BUTTON_ON, MENU_NARROW_BUTTON_OFF, x, y, 2, 1, text, on_action)
