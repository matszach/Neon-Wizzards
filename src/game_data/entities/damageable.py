from src.game_data.entities.particles.particle import Particle
from src.controllers.views import imginfo as ig
from random import random
from src.controllers.entity_handlers import AC_PARTICLES
from math import floor

DMG_SPRITES = {
    0: ig.PARTICLE_DMG_GRAY,
    1: ig.PARTICLE_DMG_RED,
    2: ig.PARTICLE_DMG_CYAN,
    3: ig.PARTICLE_DMG_DBLUE,
    4: ig.PARTICLE_DMG_YELLOW,
    5: ig.PARTICLE_DMG_DBLUE,
    6: ig.PARTICLE_DMG_GREEN
}


# parent class to all entities that can be damaged (player, monsters, breakable obstacles)
class Damageable:

    @staticmethod
    def damage_animation(x, y, dmg, dmg_type):

        # number of particles based on amount of damage taken
        nof_particles = 1 + floor(dmg/5)

        # sprite type (color) chosen based on damage type
        particle_spriteset = DMG_SPRITES[dmg_type]

        # TODO damage flash projectile superclass, damage numbers as particle here
        for i in range(nof_particles):
            p = Particle(particle_spriteset, random() * 360, velocity=0.05, duration=30)
            p.move_to(x, y)
            AC_PARTICLES.append(p)

    def take_damage(self, dmg, dmg_type=0):

        # reduces taken damage by appropriate defence
        post_def_damage = dmg - self.defences[dmg_type]

        # still, the damage taken from an attack cannot be less than 1
        post_def_damage = 1 if post_def_damage < 1 else post_def_damage

        # the damage is applied
        self.curr_hp -= post_def_damage

        # damage animation is triggered, all damageable entities have an X and Y field
        self.damage_animation(self.x, self.y, dmg, dmg_type)

    def heal(self, heal):

        # the healing is applied
        self.curr_hp += heal

        # current hp cannot exceed maximum hp
        self.curr_hp = self.max_hp if self.curr_hp > self.max_hp else self.curr_hp

    def is_dead(self):
        return self.curr_hp <= 0

    # constructor
    def __init__(self, hp=100, physical_def=0, fire_def=0, cold_def=0, lightning_def=0,
                 holy_def=0, shadow_def=0, acid_def=0):

        # entity's hit points, value of <= 0 means that the entity has been killed/destroyed
        # and should be marked as expired
        self.max_hp = hp
        self.curr_hp = hp

        # entity's defences against various types of damage
        self.defences = [
            physical_def,        # 0
            fire_def,            # 1
            cold_def,            # 2
            lightning_def,       # 3
            holy_def,            # 4
            shadow_def,          # 5
            acid_def             # 6
        ]


