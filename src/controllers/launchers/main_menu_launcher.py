import src.controllers.entity_handlers as eh
import src.controllers.gui_handlers as gh
import src.controllers.tile_handlers as th

from util.gui_elements.button import Button
from src.controllers.launchers.character_selection_launcher import launch_character_selection_menu


def launch_main_menu():

    # reset all previously active, now unneeded elements
    eh.reset()
    th.reset()
    gh.reset()

    # enables tile handlers
    eh.disable()
    th.disable()

    # TODO TEMP
    gh.active_buttons.append(Button(x=6, y=4, text='New Game',
                                    on_action=lambda: launch_character_selection_menu()))



