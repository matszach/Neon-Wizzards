from src.game_data.entities.entity import Entity
from src.controllers.entity_handlers import AC_MONSTERS, AC_OBSTACLES, AC_PROJECTILES, PLAYER
from random import randint
from math import sqrt


# parent class to all areas
class Area(Entity):

    # ===== lifecycle =====
    def passive_work(self):

        # animate every frame
        self.animate()

        # expire on duration end
        self.duration -= 1
        if self.duration <= 0:
            self.expire()

        # check for entities in range
        self.curr_range_check_interval += 1
        if self.curr_range_check_interval >= self.max_range_check_interval:

            # expire on wall collision
            if self.check_if_in_wall():
                self.expire()

            # check other collisions
            self.check_all_entity_withins()
            self.curr_range_check_interval = 0

    # ===== effects on entities =====
    # describes effect on a character withing areas range
    def on_character_within(self, character):
        pass

    # describes effect on a obstacle withing areas range
    def on_obstacle_within(self, obstacle):
        pass

    # describes effect on a projectile withing areas range
    def on_projectile_within(self, projectile):
        pass

    # check collisions
    def check_all_entity_withins(self):

        # player
        if self.affect_player:
            if self.check_if_in_range(PLAYER[0]):
                self.on_character_within(PLAYER[0])
                self.on_affect()

        # monsters
        if self.affect_monsters:
            for m in AC_MONSTERS:
                if self.check_if_in_range(m):
                    self.on_character_within(m)
                    self.on_affect()

        # obstacles
        if self.affect_obstacles:
            for o in AC_OBSTACLES:
                if self.check_if_in_range(o):
                    self.on_obstacle_within(o)
                    self.on_affect()

        # projectiles
        if self.affect_projectiles:
            for p in AC_PROJECTILES:
                if self.check_if_in_range(p):
                    self.on_projectile_within(p)
                    self.on_affect()

    # checks if target entity is in range of the area (different than check_collision(), because areas are considered
    # circles for the purpose of detecting collisions
    # area's collision size is considered it's radius of effect
    def check_if_in_range(self, entity):
        return sqrt(abs(entity.x - self.x)**2 + abs(entity.y - self.y)**2) <= self.collision_size

    # effects that affecting an entity has on the area (shrink, grow, weaken effect, increase duration ...)
    def on_affect(self):
        pass

    # constructor
    def __init__(self, sprite_set, display_size=2, collision_size=2, animation_timer=20,
                 duration=300, range_check_interval=30,
                 affect_player=False, affect_monsters=False, affect_obstacles=False, affect_projectiles=False):

        # super constructor
        Entity.__init__(self, sprite_set, display_size, collision_size, animation_timer)

        # duration left before the area expires
        self.duration = duration

        # how often the projectile checks for collisions (measured in frames)
        self.max_range_check_interval = range_check_interval
        self.curr_range_check_interval = randint(0, range_check_interval)

        # if true - will check collision for given entity type
        self.affect_player = affect_player
        self.affect_monsters = affect_monsters
        self.affect_obstacles = affect_obstacles
        self.affect_projectiles = affect_projectiles
