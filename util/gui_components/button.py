# from src.view_handlers.view_constants import unit_size as unit
# from src.view_handlers.view_handler import main_game_screen as screen
# from src.gui.elements.gui_element import GuiElement
# import pygame
#
#
# """
# Pygame has no built in buttons.
# This is my workaround.
# - listen() method needs to be called every frame in main game loop
# - the button can be instantiated like this:
# 1) b = Button()
# b.action = lambda: print('my method goes here')
# 2) b = Button(action=lambda: print('my method goes here'))
# """
#
#
# class Button(GuiElement):
#
#     def draw_default(self):
#         rect = (self.location[0]*unit, self.location[1]*unit, self.size[0]*unit, self.size[1]*unit)
#         pygame.draw.rect(screen, self.def_color, rect)
#
#     def draw_hover_on(self):
#         rect = (self.location[0] * unit, self.location[1] * unit, self.size[0] * unit, self.size[1] * unit)
#         pygame.draw.rect(screen, self.hover_color, rect)
#
#     def draw_clicked(self):
#         rect = (self.location[0] * unit + 5, self.location[1] * unit + 5, self.size[0] * unit - 10, self.size[1] * unit - 10)
#         pygame.draw.rect(screen, self.hover_color, rect)
#
#     # returns true if mouse is over the button
#     def mouse_over(self):
#         loc = pygame.mouse.get_pos()
#         return self.location[0] <= loc[0]/unit <= self.location[0] + self.size[0] and \
#             self.location[1] <= loc[1] / unit <= self.location[1] + self.size[1]
#
#     # returns true if mouse L is pressed down
#     @staticmethod
#     def mouse_down():
#         return pygame.mouse.get_pressed()[0]
#
#     # called every frame, handles button state based on user's input
#     def listen(self):
#         if self.mouse_down():
#             if self.mouse_over():
#                 self.draw_clicked()
#                 self.clicked = True
#             else:
#                 self.draw_default()
#         else:
#             if self.mouse_over():
#                 self.draw_hover_on()
#             else:
#                 self.draw_default()
#             if self.clicked:
#                 self.clicked = False
#                 self.action()
#
#     # constructor
#     def __init__(self, location=(0, 0), size=(4, 1), color=(0, 0, 255), text='button', action=lambda: None):
#
#         # button display constants
#         self.location = location
#         self.size = size
#         self.def_color = (color[0]*0.8, color[1]*0.8, color[2]*0.8)
#         self.hover_color = (color[0], color[1], color[2])
#         self.text = text
#
#         # marks button as pressed
#         self.clicked = False
#
#         # placeholder for button's 'on-click-and-release' method
#         # can be overridden with a lambda or in a child class
#         self.action = action
#
