from src.game_data.abilities.ability import Ability


# parent class to all abilities available to the player
class PlayerAbility(Ability):

    # constructor
    def __init__(self, icon, user, sprite_row_num=1, frame_counters=(2, 5, 5, 2), cooldown=0, mp_cost=0, hp_cost=0):

        # super constructor
        Ability.__init__(self, user, sprite_row_num, frame_counters, cooldown, mp_cost, hp_cost)

        # icon for display
        self.icon = icon
