from util.gui_elements.gui_element import GuiElement
from src.controllers.views.viewinfo import unit_size
from pygame import mouse


class Button(GuiElement):

    def listen(self):
        if self.is_mouse_down() and self.is_mouse_on():
            self.action()

    def is_mouse_on(self):
        u = unit_size[0]
        pos_x, pos_y = mouse.get_pos()
        return self.x < pos_x/u < self.x + self.width and self.y < pos_y/u < self.y + self.height

    @staticmethod
    def is_mouse_down():
        return mouse.get_pressed()[0]

    def draw_self(self, surface):

        u = unit_size[0]

        if self.is_mouse_on():
            # draw highlighted
            pass
        else:
            # draw un-highlighted
            pass

    # constructor
    def __init__(self, x=0, y=0, width=6, height=1, text='Button', on_action=lambda: None):

        # super constructor
        GuiElement.__init__(self, x, y)

        # button's dimensions
        self.width = width
        self.height = height

        # button's text
        self.text = text

        # button's on-click action
        self.action = on_action


