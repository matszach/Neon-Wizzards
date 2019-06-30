from src.game_data.entities.characters.player.player import PlayerCharacter
from src.controllers.views.imginfo import PLAYER_ESTERA
import src.game_data.complete_sets.complete_player_characters.estera.estera_levelup_manager as elm


# Estera's default / starting state
COL_SIZE = 0.8

COLD_DEF = 3
FIRE_DEF = -1

HP = 70
MP = 130

SPEED = 0.04

STR = 3
DEX = 5
INT = 7


class PlayerCharacterEstera(PlayerCharacter):

    # constructor
    def __init__(self):

        # super constructor
        PlayerCharacter.__init__(self, sprite_set=PLAYER_ESTERA,
                                 collision_size=COL_SIZE,
                                 fire_def=FIRE_DEF, cold_def=COLD_DEF, hp=HP, mp=MP, speed=SPEED,
                                 strength=STR, dexterity=DEX, intelligence=INT)

        # base skills
        elm.get_talent(1, 1, self)
        elm.get_talent(1, 2, self)
        elm.get_talent(1, 3, self)

