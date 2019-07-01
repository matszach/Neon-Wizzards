from src.game_data.abilities.ability import Ability
from src.game_data.abilities.projectile_using import ProjectileUsing
from random import randint


# parent class to all abilities that produce a single projectile
class SingleProjectileAbility(Ability, ProjectileUsing):

    # should be overridden
    def build_projectile(self, origin_entity, direction):
        pass

    # generate accuracy_offset
    def get_offset(self):
        return randint(-self.accuracy, self.accuracy)

    # activation
    def take_effect(self):
        self.launch_projectile(self.user, self.user.dir + self.get_offset())

    # constructor
    def __init__(self, user, projectile_class,
                 sprite_row_num=1, frame_counters=(2, 5, 5, 2), cooldown=0, mp_cost=0, hp_cost=0,
                 spawn_distance=0.5,
                 accuracy=0):

        # super constructors
        Ability.__init__(self, user, sprite_row_num, frame_counters, cooldown, mp_cost, hp_cost)
        ProjectileUsing.__init__(self, projectile_class, spawn_distance)

        # possible offset in produced projectile direction
        self.accuracy = accuracy
