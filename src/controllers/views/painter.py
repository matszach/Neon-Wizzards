import pygame
from src.controllers.views.viewinfo import unit_size as unit
from src.controllers.views.viewinfo import current_usable_window_space as cws
from src.controllers.views.imginfo import TILESET_1
from math import sin, cos, pi, ceil


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


"""
Is unique as it's position is always in the center of the screen.
Tiles and other entities are drawn based on player's location.
"""


def paint_player(surface, player):

    u = unit[0]

    # choose player's bottom sprite
    bot_sprite = get_bot_sprite(player)
    top_sprite = get_top_sprite(player)

    # scale based on player's display size
    scale = round(player.display_size * u)
    bot_sprite = pygame.transform.scale(bot_sprite, (scale, scale))
    top_sprite = pygame.transform.scale(top_sprite, (scale, scale))
    
    # rotate based on player's dir
    # ( needs adjustments as it cause image to slide back and forth. Must rotate based on center)
    angle = - player.dir
    bot_sprite = pygame.transform.rotate(bot_sprite, angle)
    top_sprite = pygame.transform.rotate(top_sprite, angle)

    # set origin based on player's location and display size
    q = abs((angle % 90))*pi/180
    off = (sin(q) + cos(q) - 1)*player.display_size

    # OLD - absolute location
    # origin = (cws[0] + (player.x-player.display_size/2 - off/2) * u,
    #           cws[1] + (player.y-player.display_size/2 - off/2) * u)

    # NEW - centered
    origin = (cws[0] + cws[2]/2 + (- player.display_size / 2 - off / 2) * u,
              cws[1] + cws[3]/2 + (- player.display_size / 2 - off / 2) * u)

    # draws sprites
    surface.blit(bot_sprite, origin)
    surface.blit(top_sprite, origin)


def paint_monster(surface, monster, player_x, player_y):
    
    u = unit[0]

    # choose player's bottom sprite
    bot_sprite = get_bot_sprite(monster)
    top_sprite = get_top_sprite(monster)

    # scale based on monster's display size
    scale = round(monster.display_size * u)
    bot_sprite = pygame.transform.scale(bot_sprite, (scale, scale))
    top_sprite = pygame.transform.scale(top_sprite, (scale, scale))

    # rotate based on monster's dir
    # ( needs adjustments as it cause image to slide back and forth. Must rotate based on center)
    angle = - monster.dir
    bot_sprite = pygame.transform.rotate(bot_sprite, angle)
    top_sprite = pygame.transform.rotate(top_sprite, angle)

    # set origin based on monster's location and display size
    q = abs((angle % 90)) * pi / 180
    off = (sin(q) + cos(q) - 1) * monster.display_size

    # NEW - centered
    origin = (cws[0] + cws[2] / 2 + (monster.x - monster.display_size / 2 - player_x - off / 2) * u,
              cws[1] + cws[3] / 2 + (monster.y - monster.display_size / 2 - player_y - off / 2) * u)

    # draws sprites
    surface.blit(bot_sprite, origin)
    surface.blit(top_sprite, origin)


def paint_entity(surface, entity, player_x, player_y):

    u = unit[0]

    # choose entity's bottom sprite
    sprite = get_bot_sprite(entity)

    # scale based on entity's display size
    scale = round(entity.display_size * u)
    sprite = pygame.transform.scale(sprite, (scale, scale))

    # rotate based on entity's dir
    # ( needs adjustments as it cause image to slide back and forth. Must rotate based on center)
    angle = - entity.dir
    sprite = pygame.transform.rotate(sprite, angle)

    # set origin based on player's location and display size
    q = abs((angle % 90)) * pi / 180
    off = (sin(q) + cos(q) - 1) * entity.display_size

    # move based on player's location
    origin = (cws[0] + cws[2] / 2 + (entity.x - entity.display_size/2 - player_x - off / 2) * u,
              cws[1] + cws[3] / 2 + (entity.y - entity.display_size/2 - player_y - off / 2) * u)

    # draws sprite
    surface.blit(sprite, origin)


def paint_tile(surface, x, y, tile_id, player_x, player_y):

    u = unit[0]

    # ===== root tiles =====
    tile = TILESET_1[tile_id[1]][tile_id[0]]

    # scale to unit
    scale = ceil(u)
    tile = pygame.transform.scale(tile, (scale, scale))

    # draws tiles
    origin = (cws[0] + cws[2]/2 + (x-0.5-player_x)*u, cws[1] + cws[3]/2 + (y-0.5-player_y)*u)
    surface.blit(tile, origin)

    # ===== corner tiles
    if tile_id[2]:
        tile = TILESET_1[4][0]
        tile = pygame.transform.scale(tile, (scale, scale))
        surface.blit(tile, origin)

    if tile_id[3]:
        tile = TILESET_1[4][1]
        tile = pygame.transform.scale(tile, (scale, scale))
        surface.blit(tile, origin)

    if tile_id[4]:
        tile = TILESET_1[4][3]
        tile = pygame.transform.scale(tile, (scale, scale))
        surface.blit(tile, origin)

    if tile_id[5]:
        tile = TILESET_1[4][2]
        tile = pygame.transform.scale(tile, (scale, scale))
        surface.blit(tile, origin)

