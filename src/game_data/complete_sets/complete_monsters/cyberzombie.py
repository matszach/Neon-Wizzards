from src.game_data.entities.characters.monsters.monster import Monster
from src.controllers.views.imginfo import MONSTER_CYBERZOMBIE
from src.game_data.abilities.monster_oriented.monster_melee_ability import MonsterMeleeAbility
from src.game_data.abilities.countersinfo import SLOW_COUNTER
from random import randint


# constants
ATTACK_INIT_RANGE = 1.5


# CyberZombie Monster class
class CyberZombie(Monster):

    def active_work(self):

        # perform active actions only when alert
        if self.alert:

            # while the monster's attack is in use the monster doesn't change direction of it's movement
            if self.abilities[self.ability_chosen].in_use:
                self.character_travel(self.dir)

            # if the ability is not in use
            else:
                # check distance to the player and consider starting an attack
                if self.get_dir_and_distance_to_player()[1] < ATTACK_INIT_RANGE:
                    self.use_chosen_ability()

                # and no matter what walk directly at them
                self.walk_directly_to_player()

        # otherwise check for player visibility
        else:

            # put monster on alert if the player has been spotted
            if self.sees_player():
                self.alert = True

    def on_expire(self):
        nof_gibs = randint(3, 6)
        self.gibbing_animation(nof_gibs, [0, 1, 2, 3, 4, 5])

    # constructor
    def __init__(self, dif_mod=1):

        # * difficulty mod gets applied in Monster's constructor

        # super constructor
        Monster.__init__(self, sprite_set=MONSTER_CYBERZOMBIE, display_size=1, collision_size=0.85, animation_timer=18,
                         hp=70, physical_def=2, fire_def=0, cold_def=1,
                         lightning_def=0, holy_def=-3, shadow_def=2, acid_def=0,
                         mp=10, speed=0.02, strength=5, dexterity=3, intelligence=1, flying=False,
                         dif_mod=dif_mod, pathing_increment=30, sight_range=8)

        self.abilities.append(CyberZombieMeleeAttack(self))


# Abilities
class CyberZombieMeleeAttack(MonsterMeleeAbility):

    # constructor
    def __init__(self, user):

        # super constructor
        MonsterMeleeAbility.__init__(self, user=user, sweep_range=1, sprite_row_num=1, frame_counters=SLOW_COUNTER,
                                     attribute_used=0, base_multiplier=2, random_multiplier=2, damage_type=0)
