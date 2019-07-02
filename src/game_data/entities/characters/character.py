from src.game_data.entities.entity import Entity
from src.game_data.entities.damageable import Damageable
from src.controllers.states.levelinfo import get_field_at
from math import sqrt


# parent class to all characters (monsters, allies, player characters)
class Character(Entity, Damageable):

    # ===== lifecycle =====
    def passive_work(self):
        self.tick_cooldowns()
        self.tick_banes()
        self.tick_boons()
        self.abilities[self.ability_chosen].continue_usage()
        if self.is_dead():
            self.expire()

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
    def has_mp(self, amt):
        return self.curr_mp >= amt

    def pay_mp(self, amt):
        self.curr_mp -= amt
        if self.curr_mp <= 0:
            self.curr_mp = 0

    def has_hp(self, amt):
        return self.curr_hp > amt  # ! not equals, no killing yourself with ability cost

    def pay_hp(self, amt):
        self.curr_hp -= amt
        if self.curr_hp <= 0:
            self.curr_hp = 0

    def tick_cooldowns(self):
        for a in self.abilities:
            a.tick_cooldown()

    def switch_to_ability(self, ability_num):

        # prevents switching to the same ability for rapid re-use
        if ability_num == self.ability_chosen:
            return

        # does not follow through with the switch if current ability is mid-use
        # allows switching during it's final stage
        if not self.abilities[self.ability_chosen].in_use and not self.abilities[self.ability_chosen].stage == 3:

            # does not follow through if an out of bounds ability is requested
            # todo this might be altered once ability bars are made
            if len(self.abilities) - 1 >= ability_num:
                self.ability_chosen = ability_num

    def use_chosen_ability(self):
        ability = self.abilities[self.ability_chosen]
        if not ability.in_use and not ability.on_cooldown():
            if self.has_mp(ability.mp_cost) and self.has_hp(ability.hp_cost):
                self.pay_mp(ability.mp_cost)
                self.pay_hp(ability.hp_cost)
                ability.use()

    def continue_action_in_progress(self):
        self.abilities[self.ability_chosen].continue_usage()

    # ===== travel =====
    def character_travel(self, direction):
        self.animate()
        if self.flying:
            self.travel_air(direction, self.speed)
        else:
            self.travel_ground(direction, self.speed)

    # ===== misc =====
    # returns True if the character has a direct line of sight of the specified point on the map
    def sees_location(self, x_targ, y_targ, max_distance):

        x_range = self.x - x_targ
        y_range = self.y - y_targ

        # if out of range - no need to check visibility
        if sqrt(x_range**2 + y_range**2) > max_distance:
            return False

        if x_range > y_range:
            x_range = round(x_range)
            for x in range(x_range):
                y = round(x / x_range * y_range)
                if get_field_at(x, y) == 1:
                    return False
        else:
            y_range = round(y_range)
            for y in range(y_range):
                x = round(y / y_range * x_range)
                if get_field_at(x, y) == 1:
                    return False

        # otherwise the location is visible
        return True

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



