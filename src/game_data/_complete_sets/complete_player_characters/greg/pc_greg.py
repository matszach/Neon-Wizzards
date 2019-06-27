from src.game_data.entities.characters.player.player import PlayerCharacter
from src.controllers.views.imginfo import PLAYER_GREG


# Estera's default / starting state
COL_SIZE = 0.9

PHYS_DEF = 2

HP = 120
MP = 80

SPEED = 0.045

STR = 7
DEX = 4
INT = 4


class PlayerCharacterGreg(PlayerCharacter):

    # constructor
    def __init__(self):

        # super constructor
        PlayerCharacter.__init__(self, sprite_set=PLAYER_GREG,
                                 collision_size=COL_SIZE,
                                 physical_def=PHYS_DEF, hp=HP, mp=MP, speed=SPEED,
                                 strength=STR, dexterity=DEX, intelligence=INT)
