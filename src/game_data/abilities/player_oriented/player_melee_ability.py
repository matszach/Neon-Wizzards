from src.game_data.abilities.ability import Ability


"""
Melee Abilities should:
- have no mp or hp cost,
- have no cooldown
- (by default?) use player's strength and deal physical damage
"""


# parent class to player's melee abilities
class PlayerMeleeAbility(Ability):

    def take_effect(self):
        # todo
        print("Player's Melee Ability Takes Effect")

    # constructor
    def __init__(self, user, sweep_range=1, frame_counters=(5, 5, 5, 10), attribute_used=0):

        # super constructor
        Ability.__init__(self, user, 1, frame_counters, 0, 0, 0)
        
        # distance to potential target (monster / obstacle) in units
        self.sweep_range = sweep_range

        # attribute used to perform the attack
        # 0 - str, 1 - dex, 2 - int
        self.attribute_used = attribute_used
