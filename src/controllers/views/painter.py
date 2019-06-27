import pygame
from src.controllers.views.viewinfo import unit_size as unit
from src.controllers.views.viewinfo import current_usable_window_space as cws
from math import sin, cos, pi


# helper methods for choosing sprites for characters
def get_bot_sprite(character):

    j = 1  # default
    if character.animation_stage == 1:
        j = 2  # left
    elif character.animation_stage == 3:
        j = 3  # right

    return character.sprite_set[0][j]


def get_top_sprite(character):

    i = character.abilities[character.ability_chosen].sprite_row_num
    j = character.abilities[character.ability_chosen].stage
    return character.sprite_set[i][j]


def paint_player(surface, player):

    u = unit[0]

    # player should always be displayed in the middle of the screen todo
    x_mod = 0
    y_mod = 0

    # choose player's bottom sprite
    bottom_sprite = get_bot_sprite(player)
    top_sprite = get_top_sprite(player)

    # convert to pygame surface
    pygame_bottom_sprite = pygame.image.fromstring(bottom_sprite.tobytes(), bottom_sprite.size, bottom_sprite.mode)
    pygame_top_sprite = pygame.image.fromstring(top_sprite.tobytes(), top_sprite.size, top_sprite.mode)

    # scale based on player's display size
    scale = round(player.display_size * u)
    pygame_bottom_sprite = pygame.transform.scale(pygame_bottom_sprite, (scale, scale))
    pygame_top_sprite = pygame.transform.scale(pygame_top_sprite, (scale, scale))
    
    # rotate based on player's dir
    # ( needs adjustments as it cause image to slide back and forth. Must rotate based on center)
    angle = - player.dir
    pygame_bottom_sprite = pygame.transform.rotate(pygame_bottom_sprite, angle)
    pygame_top_sprite = pygame.transform.rotate(pygame_top_sprite, angle)

    # set origin based on player's location and display size
    q = abs((angle % 90))*pi/180
    off = (sin(q) + cos(q) - 1)*player.display_size
    origin = (cws[0] + (player.x-player.display_size/2 - off/2) * u,
              cws[1] + (player.y-player.display_size/2 - off/2) * u)
    
    # draws sprites
    surface.blit(pygame_bottom_sprite, origin)
    surface.blit(pygame_top_sprite, origin)


def paint_monster(surface, monster):
    pass


def paint_entity(surface, entity):
    pass


def paint_tile(surface, x, y, tileID):
    pass


def paint_button(surface, button):
    pass
