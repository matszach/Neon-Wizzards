from src.game_data.entities.characters.monsters.monster import Monster
from src.controllers.views.imginfo import MONSTER_FIRE_SHELL_IMP, MONSTER_ICE_SHELL_IMP, \
    PROJECTILE_MMISSILE_CYAN, PROJECTILE_MMISSILE_RED
from src.game_data.entities.projectiles.single_hit_damaging_projectile import SingleHitDamagingProjectile
from src.game_data.abilities.base.single_projectile_ability import SingleProjectileAbility
from src.game_data.abilities.monster_oriented.monster_melee_ability import MonsterMeleeAbility
from src.game_data.abilities.countersinfo import FAST_COUNTER
from random import randint, random


# constants
MELEE_ATTACK_INIT_RANGE = 1.2
USE_RANGED_MIN_RANGE = 4
RANGED_ATTACK_COST = 5


# parent class to all shell imp subtypes
class ShellImpBASE(Monster):

    def active_work(self):

        # perform active actions only when alert
        if self.alert:

            distance = self.get_dir_and_distance_to_player()[1]
            self.face_player()

            # check distance to the player and consider starting a ranged attack
            if distance < USE_RANGED_MIN_RANGE and self.has_mp(RANGED_ATTACK_COST):
                self.switch_to_ability(1)
                self.use_chosen_ability()

            else:
                # switch to melee when the player is close
                self.switch_to_ability(0)

                # check distance to the player and consider starting a melee attack
                if distance < MELEE_ATTACK_INIT_RANGE:
                    self.use_chosen_ability()
                # and walk towards player
                self.walk_directly_to_player()

        # otherwise check for player visibility
        else:

            # put monster on alert if the player has been spotted
            if self.sees_player():
                self.alert = True

    def on_expire(self):
        nof_gibs = randint(2, 4)
        self.gibbing_animation(nof_gibs, [0, 1])

    # constructor
    def __init__(self, sprite_set, dif_mod=1, physical_def=0, fire_def=0, cold_def=0,
                 lightning_def=0, holy_def=0, shadow_def=0, acid_def=0,):

        # * difficulty mod gets applied in Monster's constructor

        # super constructor
        Monster.__init__(self, sprite_set=sprite_set, display_size=1, collision_size=0.55, animation_timer=14,
                         hp=70, physical_def=physical_def, fire_def=fire_def, cold_def=cold_def,
                         lightning_def=lightning_def, holy_def=holy_def, shadow_def=shadow_def, acid_def=acid_def,
                         mp=30, speed=0.03, strength=3, dexterity=4, intelligence=2, flying=False,
                         dif_mod=dif_mod, pathing_increment=30, sight_range=8)

        self.abilities.append(ShellImpMeleeAttack(self))


# ========== final shell imps
class FireShellImp(ShellImpBASE):

    def __init__(self, dif_mod=1):
        ShellImpBASE.__init__(self, MONSTER_FIRE_SHELL_IMP, dif_mod=dif_mod, fire_def=5)
        self.abilities.append(FireShellImpMissileAttack(self))


class IceShellImp(ShellImpBASE):

    def __init__(self, dif_mod=1):
        ShellImpBASE.__init__(self, MONSTER_ICE_SHELL_IMP, dif_mod=dif_mod, cold_def=5)
        self.abilities.append(IceShellImpMissileAttack(self))


# Projectiles
class ShellImpProjectileBASE(SingleHitDamagingProjectile):

    def calc_damage(self):
        return 0.7 + self.origin_entity.intelligence * (0.3 + 0.4 * random())

    # constructor
    def __init__(self, sprite_set, origin_entity, direction, dmg_type):

        # super constructor
        SingleHitDamagingProjectile.__init__(self, origin_entity=origin_entity,
                                             sprite_set=sprite_set, travel_direction=direction,
                                             dmg_type=dmg_type, display_size=0.9, collision_size=0.4, animation_timer=7,
                                             velocity=0.07, max_range=9, col_with_monsters=False,
                                             col_with_obstacles=True, col_with_player=True)


# final projectiles
class FireShellImpProjectile(ShellImpProjectileBASE):

    def __init__(self, origin_entity, direction):
        ShellImpProjectileBASE.__init__(self, PROJECTILE_MMISSILE_RED, origin_entity, direction, 1)


class IceShellImpProjectile(ShellImpProjectileBASE):

    def __init__(self, origin_entity, direction):
        ShellImpProjectileBASE.__init__(self, PROJECTILE_MMISSILE_CYAN, origin_entity, direction, 2)


# Abilities
class ShellImpMeleeAttack(MonsterMeleeAbility):

    # constructor
    def __init__(self, user):

        # super constructor
        MonsterMeleeAbility.__init__(self, user=user, sweep_range=0.8, sprite_row_num=1, frame_counters=FAST_COUNTER,
                                     attribute_used=1, base_multiplier=1, random_multiplier=1, damage_type=0)


class ShellImpMissileAttackBASE(SingleProjectileAbility):

    # constructor
    def __init__(self, user, projectile_class):

        # super constructor
        SingleProjectileAbility.__init__(self, user=user, projectile_class=projectile_class,
                                         sprite_row_num=1, frame_counters=FAST_COUNTER,
                                         spawn_distance=0.4, accuracy=5, cooldown=60, mp_cost=RANGED_ATTACK_COST)


class FireShellImpMissileAttack(ShellImpMissileAttackBASE):

    def __init__(self, user):
        ShellImpMissileAttackBASE.__init__(self, user, FireShellImpProjectile)


class IceShellImpMissileAttack(ShellImpMissileAttackBASE):

    def __init__(self, user):
        ShellImpMissileAttackBASE.__init__(self, user, IceShellImpProjectile)
