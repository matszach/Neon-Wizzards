from src.game_data.entities.entity import Entity
from src.game_data.entities.damageable import Damageable


# parent class to all characters (monsters, allies, player characters)
class Character(Entity, Damageable):

    # ===== lifecycle =====
    def passive_work(self):
        self.tick_cooldowns()
        self.tick_banes()
        self.tick_boons()
        self.abilities[self.ability_chosen].continue_usage()

    def active_work(self):
        pass

    # ===== conditions =====
    def apply_boon(self, condition):
        condition.start(self)
        self.boons.append(condition)

    def tick_boons(self):
        for b in self.boons:
            b.tick()
            if b.expired:
                self.boons.remove(b)

    def apply_bane(self, condition):
        condition.start(self)
        self.banes.append(condition)

    def tick_banes(self):
        for b in self.banes:
            b.tick()
            if b.expired:
                self.banes.remove(b)

    # ===== skills =====
    def tick_cooldowns(self):
        for a in self.abilities:
            a.tick_cooldown()

    def switch_to_ability(self, ability_num):

        # does not follow through with the switch if current ability is mid-use
        if not self.abilities[self.ability_chosen].in_use:

            # does not follow through if an out of bounds ability is requested
            # todo this might be altered once ability bars are made
            if len(self.abilities) - 1 >= ability_num:
                self.ability_chosen = ability_num

    def use_chosen_ability(self):
        self.abilities[self.ability_chosen].use()

    def continue_action_in_progress(self):
        self.abilities[self.ability_chosen].continue_usage()

    # ===== travel =====
    def character_travel(self, direction):
        self.animate()
        if self.flying:
            self.travel_air(direction, self.speed)
        else:
            self.travel_ground(direction, self.speed)

    # constructor
    def __init__(self, sprite_set, display_size=1, collision_size=1, animation_timer=30,
                 hp=100, physical_def=0, fire_def=0, cold_def=0, lightning_def=0,
                 holy_def=0, shadow_def=0, acid_def=0,
                 mp=100, speed=0.03, strength=5, dexterity=5, intelligence=5, flying=False):

        # super constructors
        Entity.__init__(self, sprite_set, display_size, collision_size, animation_timer)
        Damageable.__init__(self, hp, physical_def, fire_def, cold_def, lightning_def, holy_def, shadow_def, acid_def)

        # characters magical energy, fuel for most of character's skills
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

        # skills that the character has access to
        self.abilities = []
        self.ability_chosen = 0



