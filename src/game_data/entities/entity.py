from util.unit_conversion import polar_to_cartesian
from random import randint


# parent class to all entities
class Entity:

    # ===== lifecycle =====
    # called every frame for every entity
    def passive_work(self):
        # ongoing effects, collision detection here todo
        pass

    # ===== animation =====
    def animate(self):
        self.current_animation_timer += 1
        if self.current_animation_timer > self.animation_timer:
            self.current_animation_timer = 0
            self.animation_stage += 1
            if self.animation_stage >= 4:
                self.animation_stage = 0

    # ===== expiration / finalisation =====
    def on_expire(self):
        pass

    def expire(self):
        self.expired = True
        self.on_expire()

    # ===== movement =====
    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction, distance):
        x, y = polar_to_cartesian(direction, distance)
        self.x += x
        self.y += y

    def travel(self, direction, distance):
        self.dir = direction
        # movement vector clipping here todo
        self.move(distance, direction)

    # ===== collision =====
    def check_collision(self, entity):
        min_distance = (self.collision_size + entity.collision_size)/2
        if abs(self.x - entity.x) > min_distance:
            return False
        elif abs(self.y - entity.y) > min_distance:
            return False
        else:
            return True

    # ===== constructor =====
    def __init__(self, sprite_set, display_size=1, collision_size=1, animation_timer=15):

        # references entity's sprite set
        self.sprite_set = sprite_set  # todo???

        # animation
        # animates character's legs, projectile movement or obstacle's idle animation
        # eg. 0 - default, 1 - left leg in front, 2 - default, 3 - right leg in front
        self.animation_stage = randint(0, 4)
        self.current_animation_timer = randint(0, animation_timer)
        self.animation_timer = animation_timer

        # current location [units]
        self.x = 0
        self.y = 0

        # facing direction [degrees]
        self.dir = 0

        # size of displayed image [units]
        self.display_size = display_size

        # size of collision "box"
        self.collision_size = collision_size

        # marks entity status, checked by entity handlers
        self.expired = False
