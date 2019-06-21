from src.game_data.entities.entity import Entity
from src.controllers.entity_handlers import AC_MONSTERS, AC_OBSTACLES, AC_PROJECTILES, PLAYER


# parent class to all projectiles
class Projectile(Entity):

    # ===== lifecycle =====
    def passive_work(self):

        # expire on max range reached
        self.travel_air(self.dir, self.v)
        self.range -= self.v
        if self.range <= 0:
            self.expire()

        # expire on wall collision
        if self.check_if_in_wall():
            self.expire()

        # check other entity collisions
        self.check_all_entity_collisions()

    # ===== collisions =====
    # describes effect of a collision with a character
    def on_character_collision(self, character):
        pass

    # describes effect of a collision with an obstacle
    def on_obstacle_collision(self, obstacle):
        pass

    # describes effect of a collision with another projectile
    def on_projectile_collision(self, projectile):
        pass

    # check collisions
    def check_all_entity_collisions(self):

        # todo expire "checker" may be needed here or in "on_[type]_collision" methods
        #  to prevent multiple collision in one collision check cycle

        # player
        if self.col_with_player:
            if self.check_collision(PLAYER[0]):
                self.on_character_collision(PLAYER[0])
                self.on_collide()

        # monsters
        if self.col_with_monsters:
            for m in AC_MONSTERS:
                if self.check_collision(m):
                    self.on_character_collision(m)
                    self.on_collide()

        # obstacles
        if self.col_with_obstacles:
            for o in AC_OBSTACLES:
                if self.check_collision(o):
                    self.on_obstacle_collision(o)
                    self.on_collide()

        # projectiles
        if self.col_with_projectiles:
            for p in AC_PROJECTILES:
                if self.check_collision(p):
                    self.on_projectile_collision(p)
                    self.on_collide()

    # effects that a collision has on the projectile (expire, slow, down, change direction ...)
    def on_collide(self):
        pass

    # constructor
    def __init__(self, sprite_set, travel_direction, display_size=0.3, collision_size=0.2, animation_timer=10,
                 velocity=0.1, max_range=10, col_check_interval=3,
                 col_with_player=False, col_with_monsters=False, col_with_obstacles=False, col_with_projectiles=False):

        # super constructor
        Entity.__init__(self, sprite_set, display_size, collision_size, animation_timer)

        # direction of projectile's travel, overrides Entity's "dir" as they serve the same purpose here
        self.dir = travel_direction

        # distance in units that the projectile travels every frame
        self.v = velocity

        # distance left before the projectile expires
        self.range = max_range

        # how often the projectile checks for collisions (measured in frames)
        self.col_check_interval = col_check_interval

        # if true - will check collision for given entity type
        self.col_with_player = col_with_player
        self.col_with_monsters = col_with_monsters
        self.col_with_obstacles = col_with_obstacles
        self.col_with_projectiles = col_with_projectiles
