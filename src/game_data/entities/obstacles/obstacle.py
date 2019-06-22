from src.game_data.entities.entity import Entity


# parent class to all obstacles
class Obstacle(Entity):

    # constructor
    def __init__(self, sprite_set, display_size=1, collision_size=1, animation_timer=15, blocks_movement=True):

        # super constructor
        Entity.__init__(self, sprite_set, display_size, collision_size, animation_timer)

        # checked for collision by characters and projectile
        self.blocks_movement = blocks_movement

