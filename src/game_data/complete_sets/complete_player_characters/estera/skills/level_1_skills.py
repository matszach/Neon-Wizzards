from src.game_data.abilities.player_oriented.player_melee_ability import PlayerMeleeAbility
from src.game_data.abilities.player_oriented.player_single_projectile_ability import PlayerSingleProjectileAbility
from src.game_data.entities.projectiles.single_hit_damaging_projectile import SingleHitDamagingProjectile
import src.game_data.abilities.countersinfo as ci
from random import random
from src.controllers.views.imginfo import ABILITIES_ESTERA_ROW_1, PROJECTILE_ICE_MISSILE


SKILL_NAMES = {
    1: 'Staff Attack',
    2: 'Frost Bolt',
    3: 'Shard Nova',
    4: 'Chilling Ray',
    5: 'Ice Armor'
}


def gain_skill(player, i):

    if i == 1:
        learn_skill_1(player)
    elif i == 2:
        learn_skill_2(player)
    elif i == 3:
        learn_skill_3(player)
    elif i == 4:
        learn_skill_4(player)
    elif i == 5:
        learn_skill_5(player)

# ===== skill 1 =====


def learn_skill_1(player):
    player.abilities.append(EsterasStaffAttack(player))


class EsterasStaffAttack(PlayerMeleeAbility):

    def __init__(self, user):
        PlayerMeleeAbility.__init__(self, user=user, icon=ABILITIES_ESTERA_ROW_1[0][0],  name=SKILL_NAMES[1],
                                    sprite_row_num=1, frame_counters=ci.MEDIUM_COUNTER,
                                    attribute_used=0, sweep_range=1.2, base_multiplier=1.8, random_multiplier=1.3)


# ===== skill 2 =====


def learn_skill_2(player):
    player.abilities.append(EsterasFrostBolt(player))


class EsterasFrostBolt(PlayerSingleProjectileAbility):

    def build_projectile(self, origin_entity, direction):
        return self.ProjectileClass(origin_entity, direction)

    def __init__(self, user):
        PlayerSingleProjectileAbility.__init__(self, user=user, icon=ABILITIES_ESTERA_ROW_1[0][1], name=SKILL_NAMES[2],
                                               sprite_row_num=2, frame_counters=ci.SLOW_COUNTER, cooldown=120,
                                               mp_cost=3, projectile_class=FrostBoltPrj, accuracy=2, spawn_distance=0.4)


class FrostBoltPrj(SingleHitDamagingProjectile):

    def calc_damage(self):
        return 8 + self.origin_entity.intelligence * (1 + random())

    def __init__(self, user, travel_direction):
        SingleHitDamagingProjectile.__init__(self, sprite_set=PROJECTILE_ICE_MISSILE, travel_direction=travel_direction,
                                             origin_entity=user, dmg_type=2, display_size=0.8, collision_size=0.4,
                                             animation_timer=7, velocity=0.15, max_range=7, col_check_interval=5,
                                             col_with_player=False, col_with_monsters=True,
                                             col_with_obstacles=True, col_with_projectiles=True)


# ===== skill 3 =====


def learn_skill_3(player):
    pass

# ===== skill 4 =====


def learn_skill_4(player):
    pass

# ===== skill 5 =====


def learn_skill_5(player):
    pass
