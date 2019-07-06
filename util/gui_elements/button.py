from util.gui_elements.gui_element import GuiElement
from src.controllers.views.viewinfo import unit_size
from src.controllers.views.viewinfo import current_usable_window_space as cws
from pygame import mouse
import pygame


class Button(GuiElement):

    def listen(self):
        if self.is_mouse_down() and self.is_mouse_on():
            self.action()

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

        # TODO temp (will use images)
        if self.is_mouse_on():
            pygame.draw.rect(surface, (0, 100, 0), (x, y, w, h))
        else:
            pygame.draw.rect(surface, (0, 200, 0), (x, y, w, h))

        # render text, centered around the center of the button
        font = pygame.font.Font('freesansbold.ttf', round(u/4))
        txt_surf = font.render(self.text, True, (0, 0, 0))
        txt_rect = txt_surf.get_rect()
        txt_rect.center = ((x + w / 2), (y + h / 2))
        surface.blit(txt_surf, txt_rect)

    # constructor
    def __init__(self, x=0, y=0, width=3, height=0.5, text='Button', on_action=lambda: None):

        # super constructor
        GuiElement.__init__(self, x, y)

        # button's dimensions
        self.width = width
        self.height = height

        # button's text
        self.text = text

        # button's on-click action
        self.action = on_action


