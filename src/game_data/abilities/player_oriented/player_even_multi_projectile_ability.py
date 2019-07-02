from src.game_data.abilities.base.even_multi_projectile_ability import EvenMultiProjectileAbility
from src.game_data.abilities.player_oriented.player_ability import PlayerAbility


class PlayerEvenMultiProjectileAbility(EvenMultiProjectileAbility, PlayerAbility):

    # constructor
    def __init__(self, user, projectile_class, icon, name='[No Name]',
                 sprite_row_num=1, frame_counters=(2, 5, 5, 2), cooldown=0, mp_cost=0, hp_cost=0,
                 spawn_distance=0.5, nof_projectiles=5, spread=20):

        # super constructors
        EvenMultiProjectileAbility.__init__(self, user, projectile_class, sprite_row_num, frame_counters, cooldown,
                                            mp_cost, hp_cost, spawn_distance, nof_projectiles, spread)
        PlayerAbility.__init__(self, icon, name)
