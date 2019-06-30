from PIL import Image
import pygame
import os

ISIZE = 16
SSIZE = 32
BSSIZE = 64
BORDER_WIDTH = 1

FILE_EXTENSION = '.png'


def get_image_at(image_set, x, y, img_size):
    x = x * (img_size + BORDER_WIDTH)
    y = y * (img_size + BORDER_WIDTH)
    crop_area = (x, y, x + img_size, y + img_size)
    return image_set.crop(crop_area)


def load_image_set(path):
    abs_path = f'{os.path.normpath(os.getcwd() + os.sep + os.pardir)}{os.sep}roll-initiative{os.sep}{path}'
    return Image.open(abs_path)


def create_image_table(path, x_min, x_max, y_min, y_max, img_size):

    image_set = load_image_set(path)
    image_table = [[get_image_at(image_set, x, y, img_size) for x in range(x_min, x_max)] for y in range(y_min, y_max)]

    # transform to pygame images
    # * .convert_alpha() visibly increases performance
    for row in image_table:
        for i, img in enumerate(row):
            row[i] = pygame.image.fromstring(img.tobytes(), img.size, img.mode).convert_alpha()

    return image_table


# ========= ICONS ==========
ICONSETS_PATH = f'resources{os.sep}images{os.sep}iconsets{os.sep}'

# conditions
CONDITIONS_ATTRIBUTE_BOONS = create_image_table(f'{ICONSETS_PATH}condition_icons{FILE_EXTENSION}', 0, 7, 0, 1, ISIZE)
CONDITIONS_ATTRIBUTE_BANES = create_image_table(f'{ICONSETS_PATH}condition_icons{FILE_EXTENSION}', 0, 7, 1, 2, ISIZE)
CONDITIONS_DEFENCE_BOONS = create_image_table(f'{ICONSETS_PATH}condition_icons{FILE_EXTENSION}', 0, 7, 2, 3, ISIZE)
CONDITIONS_DEFENCE_BANES = create_image_table(f'{ICONSETS_PATH}condition_icons{FILE_EXTENSION}', 0, 7, 3, 4, ISIZE)
CONDITIONS_DAMAGE_OVER_TIME = create_image_table(f'{ICONSETS_PATH}condition_icons{FILE_EXTENSION}', 0, 7, 4, 5, ISIZE)

# estera's skills
ABILITIES_ESTERA_ROW_1 = create_image_table(f'{ICONSETS_PATH}estera_abilities{FILE_EXTENSION}', 0, 5, 0, 1, ISIZE)
ABILITIES_ESTERA_ROW_2 = create_image_table(f'{ICONSETS_PATH}estera_abilities{FILE_EXTENSION}', 0, 5, 1, 2, ISIZE)
ABILITIES_ESTERA_ROW_3 = create_image_table(f'{ICONSETS_PATH}estera_abilities{FILE_EXTENSION}', 0, 5, 2, 3, ISIZE)
ABILITIES_ESTERA_ROW_4 = create_image_table(f'{ICONSETS_PATH}estera_abilities{FILE_EXTENSION}', 0, 5, 3, 4, ISIZE)
ABILITIES_ESTERA_ROW_5 = create_image_table(f'{ICONSETS_PATH}estera_abilities{FILE_EXTENSION}', 0, 5, 4, 5, ISIZE)

# LOG
print('LOG: Iconsets loaded successfully.')

# ========= SPRITES ==========
SPRITESETS_PATH = f'resources{os.sep}images{os.sep}spritesets{os.sep}'

# allies
ALLIES_SPRITESETS_PATH = f'{SPRITESETS_PATH}allies{os.sep}'

# areas
AREAS_SPRITESETS_PATH = f'{SPRITESETS_PATH}areas{os.sep}'

# monsters
MONSTERS_SPRITESETS_PATH = f'{SPRITESETS_PATH}monsters{os.sep}'

MONSTER_CYBERZOMBIE = create_image_table(f'{MONSTERS_SPRITESETS_PATH}cyberzombie{FILE_EXTENSION}', 0, 4, 0, 2, SSIZE)
MONSTER_RATLING = create_image_table(f'{MONSTERS_SPRITESETS_PATH}ratling{FILE_EXTENSION}', 0, 4, 0, 2, SSIZE)


# obstacles
OBSTACLES_SPRITESETS_PATH = f'{SPRITESETS_PATH}obstacles{os.sep}'

OBSTACLE_DOOR_GREEN = create_image_table(f'{OBSTACLES_SPRITESETS_PATH}doors{FILE_EXTENSION}', 0, 4, 0, 1, SSIZE)
OBSTACLE_DOOR_RED = create_image_table(f'{OBSTACLES_SPRITESETS_PATH}doors{FILE_EXTENSION}', 0, 4, 1, 2, SSIZE)
OBSTACLE_DOOR_BLUE = create_image_table(f'{OBSTACLES_SPRITESETS_PATH}doors{FILE_EXTENSION}', 0, 4, 2, 3, SSIZE)
OBSTACLE_DOOR_BOSS = create_image_table(f'{OBSTACLES_SPRITESETS_PATH}doors{FILE_EXTENSION}', 0, 4, 3, 4, SSIZE)
OBSTACLE_DOOR_OPEN = create_image_table(f'{OBSTACLES_SPRITESETS_PATH}doors{FILE_EXTENSION}', 0, 4, 4, 5, SSIZE)

OBSTACLE_CHEST_GREEN = create_image_table(f'{OBSTACLES_SPRITESETS_PATH}chests{FILE_EXTENSION}', 0, 4, 0, 1, SSIZE)
OBSTACLE_CHEST_RED = create_image_table(f'{OBSTACLES_SPRITESETS_PATH}chests{FILE_EXTENSION}', 0, 4, 1, 2, SSIZE)
OBSTACLE_CHEST_BLUE = create_image_table(f'{OBSTACLES_SPRITESETS_PATH}chests{FILE_EXTENSION}', 0, 4, 2, 3, SSIZE)

OBSTACLE_BARREL_1 = create_image_table(f'{OBSTACLES_SPRITESETS_PATH}containers{FILE_EXTENSION}', 0, 4, 0, 1, SSIZE)
OBSTACLE_BARREL_2 = create_image_table(f'{OBSTACLES_SPRITESETS_PATH}containers{FILE_EXTENSION}', 0, 4, 1, 2, SSIZE)
OBSTACLE_CRATE_1 = create_image_table(f'{OBSTACLES_SPRITESETS_PATH}containers{FILE_EXTENSION}', 0, 4, 2, 3, SSIZE)
OBSTACLE_CRATE_2 = create_image_table(f'{OBSTACLES_SPRITESETS_PATH}containers{FILE_EXTENSION}', 0, 4, 3, 4, SSIZE)

# particles
PARTICLES_SPRITESETS_PATH = f'{SPRITESETS_PATH}{os.sep}particles{os.sep}'

# pickups
PICKUPS_SPRITESETS_PATH = f'{SPRITESETS_PATH}{os.sep}pickups{os.sep}'

PICKUP_KEY_GREEN = create_image_table(f'{PICKUPS_SPRITESETS_PATH}keys{FILE_EXTENSION}', 0, 4, 0, 1, SSIZE)
PICKUP_KEY_RED = create_image_table(f'{PICKUPS_SPRITESETS_PATH}keys{FILE_EXTENSION}', 0, 4, 1, 2, SSIZE)
PICKUP_KEY_BLUE = create_image_table(f'{PICKUPS_SPRITESETS_PATH}keys{FILE_EXTENSION}', 0, 4, 2, 3, SSIZE)
PICKUP_KEY_BOSS = create_image_table(f'{PICKUPS_SPRITESETS_PATH}keys{FILE_EXTENSION}', 0, 4, 3, 4, SSIZE)

PICKUP_CRUMB_HP = create_image_table(f'{PICKUPS_SPRITESETS_PATH}crumbs{FILE_EXTENSION}', 0, 4, 0, 1, SSIZE)
PICKUP_CRUMB_MP = create_image_table(f'{PICKUPS_SPRITESETS_PATH}crumbs{FILE_EXTENSION}', 0, 4, 1, 2, SSIZE)
PICKUP_CRUMB_EXP = create_image_table(f'{PICKUPS_SPRITESETS_PATH}crumbs{FILE_EXTENSION}', 0, 4, 2, 3, SSIZE)

# player characters
PLAYER_SPRITESETS_PATH = f'{SPRITESETS_PATH}{os.sep}player_characters{os.sep}'

PLAYER_GREG = create_image_table(f'{PLAYER_SPRITESETS_PATH}greg{FILE_EXTENSION}', 0, 4, 0, 4, SSIZE)
PLAYER_ESTERA = create_image_table(f'{PLAYER_SPRITESETS_PATH}estera{FILE_EXTENSION}', 0, 4, 0, 4, SSIZE)

# projectiles
PROJECTILES_SPRITESETS_PATH = f'{SPRITESETS_PATH}{os.sep}projectiles{os.sep}'

PROJECTILE_BULLET_GRAY = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}bullet{FILE_EXTENSION}', 0, 4, 0, 1, SSIZE)
PROJECTILE_BULLET_RED = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}bullet{FILE_EXTENSION}', 0, 4, 1, 2, SSIZE)
PROJECTILE_BULLET_YELLOW = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}bullet{FILE_EXTENSION}', 0, 4, 2, 3, SSIZE)
PROJECTILE_BULLET_GREEN = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}bullet{FILE_EXTENSION}', 0, 4, 3, 4, SSIZE)
PROJECTILE_BULLET_CYAN = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}bullet{FILE_EXTENSION}', 0, 4, 4, 5, SSIZE)
PROJECTILE_BULLET_DBLUE = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}bullet{FILE_EXTENSION}', 0, 4, 5, 6, SSIZE)

PROJECTILE_ARROW_GRAY = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}arrow{FILE_EXTENSION}', 0, 4, 0, 1, SSIZE)
PROJECTILE_ARROW_RED = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}arrow{FILE_EXTENSION}', 0, 4, 1, 2, SSIZE)
PROJECTILE_ARROW_YELLOW = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}arrow{FILE_EXTENSION}', 0, 4, 2, 3, SSIZE)
PROJECTILE_ARROW_GREEN = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}arrow{FILE_EXTENSION}', 0, 4, 3, 4, SSIZE)
PROJECTILE_ARROW_CYAN = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}arrow{FILE_EXTENSION}', 0, 4, 4, 5, SSIZE)
PROJECTILE_ARROW_DBLUE = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}arrow{FILE_EXTENSION}', 0, 4, 5, 6, SSIZE)

PROJECTILE_ICE_MISSILE = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}ice{FILE_EXTENSION}', 0, 4, 0, 1, SSIZE)
PROJECTILE_ICE_STAR = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}ice{FILE_EXTENSION}', 0, 4, 1, 2, SSIZE)
PROJECTILE_ICE_ORB = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}ice{FILE_EXTENSION}', 0, 4, 2, 3, SSIZE)
PROJECTILE_ICE_SPIKE = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}ice{FILE_EXTENSION}', 0, 4, 3, 4, SSIZE)
PROJECTILE_ICE_CRESCENT = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}ice{FILE_EXTENSION}', 0, 4, 4, 5, SSIZE)
PROJECTILE_ICE_FLAME = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}ice{FILE_EXTENSION}', 0, 4, 5, 6, SSIZE)


# LOG
print('LOG: Spritesets loaded successfully.')


# ========= TILES ==========
TILESETS_PATH = f'resources{os.sep}images{os.sep}tilesets{os.sep}'

TILESET_1 = create_image_table(f'{TILESETS_PATH}tileset_1{FILE_EXTENSION}', 0, 8, 0, 10, SSIZE)


# LOG
print('LOG: Tilesets loaded successfully.')
