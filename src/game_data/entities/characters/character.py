from src.game_data.entities.entity import Entity
from src.game_data.entities.damageable import Damageable


# parent class to all characters (monsters, allies, player characters)
class Character(Entity, Damageable):

    # ===== lifecycle =====
    def passive_work(self):
        pass  # TODO

    def active_work(self):
        pass

    # ===== upkeep =====
    def tick_cooldowns(self):
        pass  # TODO

    def tick_boons(self):
        pass  # TODO

    def tick_banes(self):
        pass  # TODO

    def continue_action_in_progress(self):
        pass  # TODO

    # ===== actions =====
    def switch_to_action(self, action_num):
        pass  # TODO

    # constructor
    def __init__(self, sprite_set, display_size=1, collision_size=1, animation_timer=15,
                 hp=100, physical_def=0, fire_def=0, cold_def=0, lightning_def=0,
                 holy_def=0, shadow_def=0, acid_def=0,
                 mp=100, speed=0.1, strength=5, dexterity=5, intelligence=5, flying=False):

        # super constructors
        Entity.__init__(self, sprite_set, display_size, collision_size, animation_timer)
        Damageable.__init__(self, hp, physical_def, fire_def, cold_def, lightning_def, holy_def, shadow_def, acid_def)

        # characters magical energy, fuel for most of character's abilities
        self.max_mp = mp
        self.curr_mp = mp

        # characters movement speed in units per frame
        self.speed = speed

        # character power attributes
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence

        # flying characters can cross chasms and may be immune to some effects
        self.flying = flying

        # positive (boons) and negative (banes) ongoing effects
        self.boons = []
        self.banes = []

        # abilities that the character has access to
        self.abilities = []
        self.action_chosen = 0



