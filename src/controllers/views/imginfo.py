from PIL import Image
import os

ISIZE = 16
SSIZE = 32
BSSIZE = 64
BORDER_WIDTH = 1


def get_image_at(image_set, x, y, img_size):
    x = x * (img_size + BORDER_WIDTH)
    y = y * (img_size + BORDER_WIDTH)
    crop_area = (x, y, x + img_size, y + img_size)
    return image_set.crop(crop_area)


def load_image_set(path):
    abs_path = f'{os.path.normpath(os.getcwd() + os.sep + os.pardir)}\\roll-initiative\\{path}'
    return Image.open(abs_path)


def create_image_table(path, x_min, x_max, y_min, y_max, img_size):
    image_set = load_image_set(path)
    image_table = [[get_image_at(image_set, x, y, img_size) for x in range(x_min, x_max)] for y in range(y_min, y_max)]
    return image_table


# ========= ICONS ==========


# ========= SPRITES ==========
SPRITESETS_PATH = 'resources\\images\\spritesets'

# allies
ALLIES_SPRITESETS_PATH = f'{SPRITESETS_PATH}\\allies'

# areas
AREAS_SPRITESETS_PATH = f'{SPRITESETS_PATH}\\areas'

# monsters
MONSTERS_SPRITESETS_PATH = f'{SPRITESETS_PATH}\\monsters'

# obstacles
OBSTACLES_SPRITESETS_PATH = f'{SPRITESETS_PATH}\\obstacles'

# particles
PARTICLES_SPRITESETS_PATH = f'{SPRITESETS_PATH}\\particles'

# pickups
PICKUPS_SPRITESETS_PATH = f'{SPRITESETS_PATH}\\pickups'

PICKUP_KEY_GREEN = create_image_table(f'{PICKUPS_SPRITESETS_PATH}\\keys.png', 0, 4, 0, 1, SSIZE)
PICKUP_KEY_RED = create_image_table(f'{PICKUPS_SPRITESETS_PATH}\\keys.png', 0, 4, 1, 2, SSIZE)
PICKUP_KEY_BLUE = create_image_table(f'{PICKUPS_SPRITESETS_PATH}\\keys.png', 0, 4, 2, 3, SSIZE)
PICKUP_KEY_BOSS = create_image_table(f'{PICKUPS_SPRITESETS_PATH}\\keys.png', 0, 4, 3, 4, SSIZE)

PICKUP_CRUMB_HP = create_image_table(f'{PICKUPS_SPRITESETS_PATH}\\crumbs.png', 0, 4, 0, 1, SSIZE)
PICKUP_CRUMB_MP = create_image_table(f'{PICKUPS_SPRITESETS_PATH}\\crumbs.png', 0, 4, 1, 2, SSIZE)
PICKUP_CRUMB_EXP = create_image_table(f'{PICKUPS_SPRITESETS_PATH}\\crumbs.png', 0, 4, 2, 3, SSIZE)

# player characters
PLAYER_SPRITESETS_PATH = f'{SPRITESETS_PATH}\\player_characters'

PLAYER_GREG = create_image_table(f'{PLAYER_SPRITESETS_PATH}\\greg_the_muscle_wizard.png', 0, 4, 0, 4, SSIZE)
PLAYER_ESTERA = create_image_table(f'{PLAYER_SPRITESETS_PATH}\\estera_the_blizzard_wizard.png', 0, 4, 0, 4, SSIZE)

# projectiles
PROJECTILES_SPRITESETS_PATH = f'{SPRITESETS_PATH}\\projectiles'

PROJECTILE_ICE_MISSILE = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}\\ice_projectiles.png', 0, 4, 0, 1, SSIZE)
PROJECTILE_ICE_STAR = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}\\ice_projectiles.png', 0, 4, 1, 2, SSIZE)
PROJECTILE_ICE_ORB = create_image_table(f'{PROJECTILES_SPRITESETS_PATH}\\ice_projectiles.png', 0, 4, 2, 3, SSIZE)


