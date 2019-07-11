from src.game_data.entities.obstacles.destroyable import Destroyable
from src.game_data.entities.pickup_dropping import PickupDropping
from src.controllers.views.imginfo import OBSTACLE_BARREL_1, OBSTACLE_BARREL_2, OBSTACLE_CRATE_1, OBSTACLE_CRATE_2

SPRITE_DICT = {
    0: OBSTACLE_BARREL_1,
    1: OBSTACLE_BARREL_2,
    2: OBSTACLE_CRATE_1,
    3: OBSTACLE_CRATE_2
}


class DestroyablePickupContainer(Destroyable, PickupDropping):

    # activated when the container is destroyed
    def on_expire(self):
        self.drop_all_items()
        # todo animation

    # constructor
    def __init__(self, sprite_set_type=0, display_size=1, collision_size=1, animation_timer=15,
                 blocks_movement=True,
                 hp=50, physical_def=0, fire_def=-5, cold_def=0, lightning_def=0,
                 holy_def=0, shadow_def=0, acid_def=-5):

        # super constructor
        Destroyable.__init__(self, SPRITE_DICT[sprite_set_type], display_size, collision_size, animation_timer,
                             blocks_movement,
                             hp, physical_def, fire_def, cold_def, lightning_def, holy_def, shadow_def, acid_def)
        PickupDropping.__init__(self)

