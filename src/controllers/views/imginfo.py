from PIL import Image
import os

sprite_size = 32

border_width = 1


def get_sprite_at(sprite_set, x, y):
    x = x * (sprite_size + border_width)
    y = y * (sprite_size + border_width)
    crop_area = (x, y, x + sprite_size, y + sprite_size)
    return sprite_set.crop(crop_area)


def load_sprite_set(path):
    abs_path = os.path.normpath(os.getcwd() + os.sep + os.pardir) + '\\' + path
    return Image.open(abs_path)


# characters
CHAR_DEFAULT = load_sprite_set('resources/spritesets/template.png')

# player characters
PLAYER_CHAR_GREG = load_sprite_set('resources/spritesets/player_characters/greg_the_muscle_wizard.png')
PLAYER_CHAR_ESTERA = load_sprite_set('resources/spritesets/player_characters/estera_the_blizzard_wizard.png')

