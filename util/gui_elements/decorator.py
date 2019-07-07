from util.gui_elements.gui_element import GuiElement
from src.controllers.views.viewinfo import unit_size
from src.controllers.views.viewinfo import current_usable_window_space as cws
import pygame


# default and not animated decorator
class Decorator(GuiElement):

    def animate(self):
        pass

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

        sprite = pygame.transform.scale(self.img, (scale_x, scale_y))

        surface.blit(sprite, (x, y, w, h))

    # constructor
    def __init__(self, img, x=0, y=0, width=1, height=1):

        # super constructor
        GuiElement.__init__(self, x, y)

        # displayed image
        self.img = img

        # decorator draw size in units
        self.width = width
        self.height = height
