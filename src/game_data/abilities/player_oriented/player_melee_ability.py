from src.game_data.abilities.base.melee_ability import MeleeAbility
from src.game_data.abilities.player_oriented.player_ability import PlayerAbility
from src.controllers.entity_handlers import AC_MONSTERS, AC_OBSTACLES
from src.game_data.entities.damageable import Damageable
from math import sqrt


# parent class to player's melee skills
class PlayerMeleeAbility(MeleeAbility, PlayerAbility):

    def take_effect(self):

        for e in AC_MONSTERS:
            if self.sweep_range > sqrt((self.user.x-e.x)**2 + (self.user.x-e.x)**2):
                e.take_damage(self.calc_damage(), self.damage_type)
                return  # only 1 target affected

        for e in AC_OBSTACLES:
            if isinstance(e, Damageable) and self.sweep_range > sqrt((self.user.x-e.x)**2 + (self.user.x-e.x)**2):
                e.take_damage(self.calc_damage(), self.damage_type)
                return  # only 1 target affected

    # constructor
    def __init__(self, user, icon, name='[Ability Name]', sweep_range=1, sprite_row_num=1, frame_counters=(5, 5, 5, 10),
                 attribute_used=0, base_multiplier=2, random_multiplier=1.5, damage_type=0):

        # super constructors
        MeleeAbility.__init__(self, user, sweep_range, sprite_row_num, frame_counters, attribute_used,
                              base_multiplier, random_multiplier, damage_type)
        PlayerAbility.__init__(self, icon, name)
