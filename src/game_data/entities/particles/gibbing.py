from src.game_data.entities.particles.particle import Particle
from src.controllers.views import imginfo as im

GIB_TYPE_SPRITE_SETS = {
    0: im.PARTICLE_GIB_RED_1,
    1: im.PARTICLE_GIB_RED_2,
    2: im.PARTICLE_GIB_GRAY_1,
    3: im.PARTICLE_GIB_GRAY_2,
    4: im.PARTICLE_GIB_GREEN_1,
    5: im.PARTICLE_GIB_GREEN_2
}


class Gibbing(Particle):

    # adding rotation
    def passive_work(self):
        self.dir += 3
        Particle.passive_work(self)

    # constructor
    def __init__(self, gib_type=0, direction=0):

        sprite_set = GIB_TYPE_SPRITE_SETS[gib_type]

        # super constructor
        Particle.__init__(self, sprite_set=sprite_set, display_size=0.8,
                          travel_direction=direction, velocity=0.02, duration=40)

