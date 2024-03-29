import src.controllers.entity_handlers as eh
import src.controllers.gui_handlers as gh
import src.controllers.tile_handlers as th
from src.controllers.level_generators.level_generator import generate_level
from src.controllers.level_generators.tile_id_generator import translate_to_tile_ids
from util.gui_elements.animation import ScreenRevealPixelation
from util.gui_elements.in_game_gui.ability_and_bar_gui import AbilityAndBarGui
from random import randint


def launch_level(player_character, level, difficulty, level_seed):

    # reset all previously active, now unneeded elements
    eh.reset()
    th.reset()
    gh.reset()

    # enables tile handlers
    eh.enable()
    th.enable()

    # set passed character as active player character
    eh.PLAYER = [player_character]

    # generates level based on its number and its desired difficulty
    generate_level(level, difficulty, player_character, level_seed)

    # update tile handler for tile IDs
    translate_to_tile_ids()

    # builds user in-game interface
    # TODO

    # screen change animation
    gh.active_animations.append(ScreenRevealPixelation())

    gh.active_decorators.append(AbilityAndBarGui())

