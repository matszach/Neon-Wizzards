from src.game_data.entities.entity import Entity
from src.controllers.entity_handlers import PLAYER


# parent class to all pickups
class Pickup(Entity):

    # ===== lifecycle =====
    def passive_work(self):

        # animate every frame
        self.animate()

        # checks collision with player
        if self.check_collision(PLAYER[0]):
            self.on_picked_up(PLAYER[0])
            self.expire()

    # effect that picking the pickup up has on the player
    def on_picked_up(self, player):
        pass

    # constructor
    def __init__(self, sprite_set, display_size=0.3, collision_size=0.4, animation_timer=15):

        # super constructor
        Entity.__init__(self, sprite_set, display_size, collision_size, animation_timer)
