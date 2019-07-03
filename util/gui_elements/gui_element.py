

# parent class to all gui elements ( Buttons, Decorators, etc)
class GuiElement:

    # gui elements each have an unique way of being drawn, therefore it makes the most not to export the draw
    # functionality to an external painter
    def draw_self(self, surface):
        pass

    # constructor
    def __init__(self, x=0, y=0):

        # element's position on game screen (in units)
        self.x = x
        self.y = y
