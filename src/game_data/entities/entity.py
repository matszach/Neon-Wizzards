from util.unit_conversion import polar_to_cartesian
from src.controllers.states.levelinfo import get_field_at
from random import randint


MAX_ANIMATION_STAGE = 4


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
        if self.current_animation_timer >= self.animation_timer:
            self.current_animation_timer = 0
            self.animation_stage += 1
            if self.animation_stage >= MAX_ANIMATION_STAGE:
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

    def move(self, x, y):
        self.x += x
        self.y += y

    def travel_ground(self, direction, distance):
        self.dir = direction
        x, y = polar_to_cartesian(direction, distance)
        x, y = self.clip_ground_movement_vector(x, y)
        self.move(x, y)

    def travel_air(self, direction, distance):
        self.dir = direction
        x, y = polar_to_cartesian(direction, distance)
        x, y = self.clip_air_movement_vector(x, y)
        self.move(x, y)

    def travel_unchecked(self, direction, distance):
        self.dir = direction
        x, y = polar_to_cartesian(direction, distance)
        self.move(x, y)

    # ===== collision =====
    def check_collision(self, entity):
        min_distance = (self.collision_size + entity.collision_size)/2
        if abs(self.x - entity.x) > min_distance:
            return False
        elif abs(self.y - entity.y) > min_distance:
            return False
        else:
            return True

    # returns true if entity's approximate location is "in wall" - meaning a field marked as "1"
    # particles and projectiles expire on wall collision
    def check_if_in_wall(self):
        return get_field_at(self.x, self.y) == 1

    # returns clipped movement vector if a wall ("1") or a pit ("2") prevents full movement
    def clip_ground_movement_vector(self, x, y):

        new_x = x
        new_y = y

        # y clipping
        yi = round(self.y + y + self.collision_size / 2 * y / abs(y))
        for xi in range(round(self.x - self.collision_size/2), round(self.x + self.collision_size/2) + 1):
            if get_field_at(xi, yi) in [1, 2]:
                if y > 0:
                    # yi - 0.5 = self.y + self.collision_size/2 + new_y (new_y is positive)
                    new_y = yi - 0.5 - self.y - self.collision_size/2
                else:
                    # yi + 0.5 = self.y - self.collision_size/2 + new_y (new_y is negative, or zero)
                    new_y = yi + 0.5 - self.y + self.collision_size/2
                break

        # x clipping
        xj = round(self.x + x + self.collision_size / 2 * x / abs(x))
        for yj in range(round(self.y - self.collision_size / 2), round(self.y + self.collision_size / 2) + 1):
            if get_field_at(xj, yj) in [1, 2]:
                if x > 0:
                    new_x = xj - 0.5 - self.x - self.collision_size / 2
                else:
                    new_x = xj + 0.5 - self.x + self.collision_size / 2
                break

        return new_x, new_y

    # as above but only for walls
    def clip_air_movement_vector(self, x, y):

        new_x = x
        new_y = y

        # y clipping
        yi = round(self.y + y + self.collision_size / 2 * y / abs(y))
        for xi in range(round(self.x - self.collision_size / 2), round(self.x + self.collision_size / 2) + 1):
            if get_field_at(xi, yi) == 1:
                if y > 0:
                    # yi - 0.5 = self.y + self.collision_size/2 + new_y (new_y is positive)
                    new_y = yi - 0.5 - self.y - self.collision_size / 2
                else:
                    # yi + 0.5 = self.y - self.collision_size/2 + new_y (new_y is negative, or zero)
                    new_y = yi + 0.5 - self.y + self.collision_size / 2
                break

        # x clipping
        xj = round(self.x + x + self.collision_size / 2 * x / abs(x))
        for yj in range(round(self.y - self.collision_size / 2), round(self.y + self.collision_size / 2) + 1):
            if get_field_at(xj, yj) == 1:
                if x > 0:
                    new_x = xj - 0.5 - self.x - self.collision_size / 2
                else:
                    new_x = xj + 0.5 - self.x + self.collision_size / 2
                break

        return new_x, new_y

    # ===== constructor =====
    def __init__(self, sprite_set, display_size=1, collision_size=1, animation_timer=15):

        # references entity's sprite set
        self.sprite_set = sprite_set  # todo???

        # animation
        # animates character's legs, projectile movement or obstacle's idle animation
        # eg. 0 - default, 1 - left leg in front, 2 - default, 3 - right leg in front
        self.animation_stage = randint(0, MAX_ANIMATION_STAGE)
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
