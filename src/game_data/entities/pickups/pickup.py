from src.game_data.entities.entity import Entity
from src.controllers.entity_handlers import PLAYER


# parent class to all pickups
class Pickup(Entity):

    # ===== lifecycle =====
    def passive_work(self):

        # animate every frame
        self.animate()

        # slide to full stop
        if self.slide_speed > 0:
            self.travel_ground(self.slide_direction, self.slide_speed)
            self.slide_speed -= self.slide_speed_drop

        # checks collision with player
        if self.check_collision(PLAYER[0]):
            self.on_picked_up(PLAYER[0])
            self.expire()

    # take_effect that picking the pickup up has on the player
    def on_picked_up(self, player):
        pass

    # constructor
    def __init__(self, sprite_set, display_size=0.6, collision_size=0.5, animation_timer=60,
                 slide_speed=0.2, slide_speed_drop=0.005, slide_direction=0):

        # super constructor
        Entity.__init__(self, sprite_set, display_size, collision_size, animation_timer)

        # initial slide values
        self.slide_speed = slide_speed
        self.slide_speed_drop = slide_speed_drop
        self.slide_direction = slide_direction
