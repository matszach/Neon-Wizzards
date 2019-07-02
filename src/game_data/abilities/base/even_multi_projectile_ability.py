from src.game_data.abilities.ability import Ability
from src.game_data.abilities.projectile_using import ProjectileUsing
from random import randint


# parent class to all abilities that produce a a evenly spread cone of projectiles
class EvenMultiProjectileAbility(Ability, ProjectileUsing):

    # should be overridden
    def build_projectile(self, origin_entity, direction):
        pass

    # activation
    def take_effect(self):
        dist = round(2*self.spread/self.nof_projectiles)
        for offset in range(-self.spread, self.spread, dist):
            self.launch_projectile(self.user, self.user.dir + offset)

    # constructor
    def __init__(self, user, projectile_class,
                 sprite_row_num=1, frame_counters=(2, 5, 5, 2), cooldown=0, mp_cost=0, hp_cost=0,
                 spawn_distance=0.5,
                 nof_projectiles=5, spread=20):

        # super constructors
        Ability.__init__(self, user, sprite_row_num, frame_counters, cooldown, mp_cost, hp_cost)
        ProjectileUsing.__init__(self, projectile_class, spawn_distance)

        # number of launched projectiles
        self.nof_projectiles = nof_projectiles

        # widths of the projectile cone
        self.spread = spread
