from src.game_data.entities.obstacles.obstacle import Obstacle
from src.game_data.entities.damageable import Damageable


# parent class to all destroyable obstacles
class Destroyable(Obstacle, Damageable):

    # ===== lifecycle =====
    def passive_work(self):

        # animate every frame
        self.animate()

        # check if the destroyable should be destroyed
        if self.is_dead():
            self.destroy()

    # ===== breaking ======
    def on_destroy(self):
        pass

    def destroy(self):
        self.expire()
        self.on_destroy()

    # constructor
    def __init__(self, sprite_set, display_size=1, collision_size=1, animation_timer=15,
                 blocks_movement=True,
                 hp=100, physical_def=0, fire_def=0, cold_def=0, lightning_def=0,
                 holy_def=0, shadow_def=0, acid_def=0):

        # super constructors
        Obstacle.__init__(self, sprite_set, display_size, collision_size, animation_timer, blocks_movement)
        Damageable.__init__(self, hp, physical_def, fire_def, cold_def, lightning_def, holy_def, shadow_def, acid_def)
