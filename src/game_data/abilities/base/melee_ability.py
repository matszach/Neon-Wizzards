from src.game_data.abilities.ability import Ability
from random import random

"""
Melee Abilities should:
- have no mp or hp cost,
- have no cooldown
- (by default?) use player's strength and deal physical damage
"""


class MeleeAbility(Ability):

    # damage calculation
    def calc_damage(self):

        if self.attribute_used == 0:
            att = self.user.strength
        elif self.attribute_used == 1:
            att = self.user.dexterity
        else:
            att = self.user.intelligence

        return self.base_multiplier * att + self.random_multiplier * random()*att

    # activation
    def take_effect(self):
        pass

    # constructor
    def __init__(self, user, sweep_range=1, sprite_row_num=1, frame_counters=(5, 5, 5, 10),
                 attribute_used=0, base_multiplier=2, random_multiplier=1.5, damage_type=0):

        # super constructors
        Ability.__init__(self, user, sprite_row_num, frame_counters, 0, 0, 0)

        # distance to potential target (monster / obstacle) in units
        self.sweep_range = sweep_range

        # attribute used to perform the attack
        # 0 - str, 1 - dex, 2 - int
        self.attribute_used = attribute_used

        # multipliers for damage calculation
        self.base_multiplier = base_multiplier
        self.random_multiplier = random_multiplier

        # type of damage dealt
        self.damage_type = damage_type
