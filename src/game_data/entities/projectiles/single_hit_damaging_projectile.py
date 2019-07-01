from src.game_data.entities.projectiles.projectile import Projectile
from src.game_data.entities.damageable import Damageable


class SingleHitDamagingProjectile(Projectile):

    # overridable damage calculator
    def calc_damage(self):
        return 0

    # on - collisions
    def on_character_collision(self, character):
        character.take_damage(self.calc_damage(), self.dmg_type)
        self.expire()

    def on_projectile_collision(self, projectile):
        pass

    def on_obstacle_collision(self, obstacle):
        if isinstance(obstacle, Damageable):
            obstacle.take_damage(self.calc_damage(), self.dmg_type)
            self.expire()

    # constructor
    def __init__(self,  sprite_set, travel_direction, origin_entity=None, dmg_type=0,
                 display_size=0.3, collision_size=0.2, animation_timer=10,
                 velocity=0.1, max_range=10, col_check_interval=3,
                 col_with_player=False, col_with_monsters=False, col_with_obstacles=False, col_with_projectiles=False):

        # super constructor
        Projectile.__init__(self, sprite_set, travel_direction, display_size, collision_size, animation_timer,
                            velocity, max_range, col_check_interval,
                            col_with_player, col_with_monsters, col_with_obstacles, col_with_projectiles)

        # reference used for damage calculation
        self.origin_entity = origin_entity

        # type of damage dealt
        self.dmg_type = dmg_type

