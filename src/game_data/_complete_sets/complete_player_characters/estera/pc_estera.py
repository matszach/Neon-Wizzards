from src.game_data.entities.characters.player.player import PlayerCharacter
from src.controllers.views.imginfo import PLAYER_ESTERA, MONSTER_CYBERZOMBIE


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

        # temp todo
        # starting abilities will be appended here
        from src.game_data.abilities.player_oriented.player_melee_ability import PlayerMeleeAbility
        import src.game_data.abilities.countersinfo as ci
        self.abilities.append(PlayerMeleeAbility(self, frame_counters=ci.MEDIUM_COUNTER))
