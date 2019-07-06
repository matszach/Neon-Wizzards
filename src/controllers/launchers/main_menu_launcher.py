import src.controllers.entity_handlers as eh
import src.controllers.gui_handlers as gh
import src.controllers.tile_handlers as th

from util.gui_elements.button import Button


# ==================================================== TEST
# fixme #
# this will, in the future, be called withing the main game loop, on button click etc.
from src.game_data.complete_sets.complete_player_characters.estera.pc_estera import PlayerCharacterEstera
from src.game_data.complete_sets.complete_player_characters.greg.pc_greg import PlayerCharacterGreg
from src.controllers.launchers.level_launcher import launch_level
# ==================================================== TEST


def launch_main_menu():

    # reset all previously active, now unneeded elements
    eh.reset()
    th.reset()
    gh.reset()

    # enables tile handlers
    eh.disable()
    th.disable()

    # TODO TEMP
    gh.active_buttons.append(Button(x=6, y=4, text='Estera',
                                    on_action=lambda: launch_level(PlayerCharacterEstera(), 1, 1)))

    gh.active_buttons.append(Button(x=6, y=5, text='Greg',
                                    on_action=lambda: launch_level(PlayerCharacterGreg(), 1, 1)))


