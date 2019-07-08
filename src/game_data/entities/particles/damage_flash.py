from src.game_data.entities.particles.particle import Particle
from src.controllers.views import imginfo as ig


DMG_SPRITES = {
    0: ig.PARTICLE_DMG_GRAY,
    1: ig.PARTICLE_DMG_RED,
    2: ig.PARTICLE_DMG_CYAN,
    3: ig.PARTICLE_DMG_DBLUE,
    4: ig.PARTICLE_DMG_YELLOW,
    5: ig.PARTICLE_DMG_DBLUE,
    6: ig.PARTICLE_DMG_GREEN
}


class DamageFlash(Particle):

    # constructor
    def __init__(self, dmg_type=0, direction=0):

        particle_spriteset = DMG_SPRITES[dmg_type]

        # super constructor
        Particle.__init__(self, sprite_set=particle_spriteset, travel_direction=direction, velocity=0.05, duration=30)

