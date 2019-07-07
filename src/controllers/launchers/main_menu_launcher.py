import src.controllers.entity_handlers as eh
import src.controllers.gui_handlers as gh
import src.controllers.tile_handlers as th

from util.gui_elements.button import WideButton
from src.controllers.launchers.character_selection_launcher import launch_character_selection_menu
from util.gui_elements.decorator import Decorator
from src.controllers.views.imginfo import MENU_LOGO


def launch_main_menu():

    # reset all previously active, now unneeded elements
    eh.reset()
    th.reset()
    gh.reset()

    # enables tile and entity handlers
    eh.disable()
    th.disable()

    # adding title-logo
    gh.active_decorators.append(Decorator(MENU_LOGO, x=3, y=1, width=10, height=2))

    # adding main menu buttons
    gh.active_buttons.append(WideButton(x=6, y=4.5, text='New Game',
                                        on_action=lambda: launch_character_selection_menu()))

    gh.active_buttons.append(WideButton(x=6, y=5.5, text='Options',
                                        on_action=lambda: None))

    gh.active_buttons.append(WideButton(x=6, y=6.5, text='About',
                                        on_action=lambda: None))

    gh.active_buttons.append(WideButton(x=6, y=7.5, text='Credits',
                                        on_action=lambda: None))

