from src.game_data.entities.characters.monsters.monster import Monster
from src.controllers.views.imginfo import MONSTER_RATLING
from src.game_data.abilities.base.single_projectile_ability import SingleProjectileAbility
from src.game_data.entities.projectiles.single_hit_damaging_projectile import SingleHitDamagingProjectile
from src.game_data.abilities.countersinfo import NEAR_INSTANT_COUNTER
from src.controllers.views.imginfo import PROJECTILE_BULLET_YELLOW

from random import randint, random


# constants
ATTACK_INIT_RANGE = 1.5


# Ratling Monster class
class Ratling(Monster):

    def active_work(self):

        # TODO MAKE THIS BETTER

        # perform active actions only when alert
        if self.alert:

            if self.sees_player():
                self.turn(self.get_dir_and_distance_to_player()[0])
                self.use_chosen_ability()
            else:
                self.walk_directly_to_player()

        else:
            # put monster on alert if the player has been spotted
            if self.sees_player():
                self.alert = True

    def on_expire(self):
        nof_gibs = randint(2, 4)
        self.gibbing_animation(nof_gibs, [0, 1, 2, 3])

    # constructor
    def __init__(self, dif_mod=1):

        # * difficulty mod gets applied in Monster's constructor

        # super constructor
        Monster.__init__(self, sprite_set=MONSTER_RATLING, display_size=1, collision_size=0.75, animation_timer=12,
                         hp=40, physical_def=0, fire_def=0, cold_def=0,
                         lightning_def=-3, holy_def=0, shadow_def=0, acid_def=2,
                         mp=20, speed=0.04, strength=2, dexterity=5, intelligence=3, flying=False,
                         dif_mod=dif_mod, pathing_increment=30, sight_range=12)

        self.abilities.append(RatlingGatling(self))


# Projectiles
class RatlingGatlingPrj(SingleHitDamagingProjectile):

    def calc_damage(self):
        return 0.2 + self.origin_entity.dexterity * (0.2 + 0.2 * random())

    # constructor
    def __init__(self, origin_entity, direction):

        # super constructor
        SingleHitDamagingProjectile.__init__(self, origin_entity=origin_entity,
                                             sprite_set=PROJECTILE_BULLET_YELLOW, travel_direction=direction,
                                             dmg_type=0, display_size=0.8, collision_size=0.2, animation_timer=10,
                                             velocity=0.11, max_range=7, col_with_monsters=False,
                                             col_with_obstacles=True, col_with_player=True)


# Abilities
class RatlingGatling(SingleProjectileAbility):

    # constructor
    def __init__(self, user):

        # super constructor
        SingleProjectileAbility.__init__(self, user=user, projectile_class=RatlingGatlingPrj,
                                         sprite_row_num=1, frame_counters=NEAR_INSTANT_COUNTER,
                                         spawn_distance=0.4, accuracy=5)


