from src.game_data.entities.entity import Entity
from src.game_data.entities.damageable import Damageable
from src.controllers.states.levelinfo import get_field_at
import src.controllers.entity_handlers as eh
from util.unit_conversion import cartesian_to_polar
from math import sqrt, ceil
from random import random, choice
from src.game_data.entities.particles.gibbing import Gibbing



# parent class to all characters ,(monsters, allies, player characters)
class Character(Entity, Damageable):

    # ===== lifecycle =====
    def passive_work(self):
        self.tick_cooldowns()
        self.tick_banes()
        self.tick_boons()
        self.repel_characters()
        self.abilities[self.ability_chosen].continue_usage()
        if self.is_dead():
            self.expire()

    def active_work(self):
        pass

    def repel_characters(self):

        # for each active character
        for e in eh.AC_MONSTERS + eh.AC_ALLIES + eh.PLAYER:

            # drop for self and drop if no collision detected
            if e is not self and self.check_collision(e):

                # repel colliding characters from each other
                x = self.x - e.x
                y = self.y - e.y
                direction = cartesian_to_polar(x, y)[0]
                self.character_travel_no_animation(direction)
                e.character_travel_no_animation(-direction)

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

    def gain_mp(self, amt):

        # the restoration is applied
        self.curr_mp += amt

        # current mp cannot exceed maximum mp
        self.curr_mp = self.max_mp if self.curr_mp > self.max_mp else self.curr_mp

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

        # does not follow through if an out of bounds ability is requested
        # todo this might be altered once ability bars are made
        if len(self.abilities) - 1 >= ability_num:

            # resets any any ability that has been switched out mid-use ( TODO THIS MIGHT ET MOVED TO ABILITY CLASS)
            self.abilities[self.ability_chosen].stage = 0
            self.abilities[self.ability_chosen].current_animation_counter = 0
            self.abilities[self.ability_chosen].in_use = False

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

    def character_travel_no_animation(self, direction):
        if self.flying:
            self.travel_air(direction, self.speed)
        else:
            self.travel_ground(direction, self.speed)

    # ===== misc =====
    # returns True if the character has a direct line of sight of the specified point on the map
    # fixme (?) (seem to kinda work now - only bugs out on single blocks of wall)
    def sees_location(self, x_targ, y_targ, max_distance):

        # true range
        x_range = self.x - x_targ
        y_range = self.y - y_targ

        # total distance
        distance = sqrt(x_range**2 + y_range**2)

        # if out of range - no need to check visibility
        if distance > max_distance:
            return False

        # absolute range
        x_abs_range = abs(x_range)
        y_abs_range = abs(y_range)

        # step for checking visibility
        if x_abs_range > y_abs_range:
            x_step = - x_range / x_abs_range  # -> 1 or -1
            y_step = - y_range / x_abs_range  # -> 0.x or -0.x
        else:
            x_step = - x_range / y_abs_range  # -> 0.x or -0.x
            y_step = - y_range / y_abs_range  # -> 1 or -1

        # check on path
        for i in range(ceil(x_abs_range)):
            x_check = self.x + i * x_step
            y_check = self.y + i * y_step
            if get_field_at(x_check, y_check) == 1:
                return False

        # otherwise the location is visible
        return True

    # ===== gibbing on death animation
    def gibbing_animation(self, nof_particles, allowed_gibs_nums):
        for i in range(nof_particles):
            p = Gibbing(choice(allowed_gibs_nums), random() * 360)
            p.move_to(self.x, self.y)
            eh.AC_PARTICLES.append(p)

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



