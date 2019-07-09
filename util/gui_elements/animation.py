from util.gui_elements.gui_element import GuiElement
from src.controllers.views.viewinfo import unit_size
from src.controllers.views.viewinfo import window_size_in_units as ws
from src.controllers.views.viewinfo import current_usable_window_space as cws
import pygame
from random import choice


# default and not animated decorator
class Animation(GuiElement):

    def draw_self(self, surface):
        pass

    def animate(self):
        pass

    def tick(self):
        self.duration_left -= 1
        if self.duration_left < 0:
            self.finished = True

    # constructor
    def __init__(self, x=0, y=0, duration=60):

        # super constructor
        GuiElement.__init__(self, x, y)

        # duration left (in frames)
        self.duration_left = duration

        # marked as finished -> will me removed from animation list
        self.finished = False


class ScreenRevealPixelation(Animation):

    # randomly remove a unit
    def animate(self):
        self.tick()
        for i in range(20):
            if not len(self.hidden) == 0:
                self.hidden.remove(choice(self.hidden))

    # draw hidden units
    def draw_self(self, surface):
        u = unit_size[0]/2
        for block in self.hidden:
            pygame.draw.rect(surface, self.color, (cws[0]+block[0]*u, cws[1]+block[1]*u, u, u))

    # constructor
    def __init__(self, color=(0, 0, 0)):

        # super constructor
        Animation.__init__(self, 0, 0, 60)

        # applied color
        self.color = color

        # currently hidden units
        self.hidden = []
        for x in range(0, 2*ws[0]):
            for y in range(0, 2*ws[1]):
                self.hidden.append((x, y))
