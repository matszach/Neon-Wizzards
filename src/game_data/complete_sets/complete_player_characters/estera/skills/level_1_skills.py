from src.game_data.abilities.player_oriented.player_melee_ability import PlayerMeleeAbility
import src.game_data.abilities.countersinfo as ci
from src.controllers.views.imginfo import ABILITIES_ESTERA_ROW_1


SKILL_NAMES = {
    1: 'Staff Attack',
    2: '[TEMP]',
    3: '[TEMP]',
    4: '[TEMP]',
    5: '[TEMP]',

}


def gain_skill(player, i):

    if i == 1:
        learn_skill_1(player)

# ===== skill 1 =====


def learn_skill_1(player):
    player.abilities.append(EsterasBasicMelee(player))


class EsterasBasicMelee(PlayerMeleeAbility):

    def __init__(self, user):
        PlayerMeleeAbility.__init__(self, user=user, icon=ABILITIES_ESTERA_ROW_1[0][0],  name=SKILL_NAMES[1],
                                    sprite_row_num=1, frame_counters=ci.MEDIUM_COUNTER,
                                    attribute_used=0, sweep_range=1.2, base_multiplier=1.8, random_multiplier=1.3)

# ===== skill 2 =====


def learn_skill_2(player):
    pass

# ===== skill 3 =====


def learn_skill_3(player):
    pass

# ===== skill 4 =====


def learn_skill_4(player):
    pass

# ===== skill 5 =====


def learn_skill_5(player):
    pass
