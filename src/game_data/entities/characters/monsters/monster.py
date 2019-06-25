from src.game_data.entities.characters.character import Character
from random import randint


# parent class to all monsters
class Monster(Character):

    # TODO a lot

    # constructor
    def __init__(self, sprite_set, display_size=1, collision_size=1, animation_timer=15,
                 hp=100, physical_def=0, fire_def=0, cold_def=0, lightning_def=0,
                 holy_def=0, shadow_def=0, acid_def=0,
                 mp=100, speed=0.1, strength=5, dexterity=5, intelligence=5, flying=False,
                 dif_mod=1, pathing_increment=30):

        # super constructors
        Character.__init__(self, sprite_set, display_size, collision_size, animation_timer,
                           hp * dif_mod, physical_def, fire_def, cold_def, lightning_def,
                           holy_def, shadow_def, acid_def,
                           mp, speed, strength, dexterity, intelligence, flying)

        # difficulty modifier, alters hp (todo and maybe more ?)
        # of the monster attributes
        # 0.5 - trivial, 0.75 - easy, 1.00 - normal, 1.25 - hard, 1.5 - insane (?)
        self.dif_mod = dif_mod

        # how often the monster checks for path
        self.max_pathing_increment = pathing_increment
        self.curr_pathing_increment = randint(0, pathing_increment)

        # current direction of movement (possibly ignored when in direct sight of the player)
        self.path_dir = 0

        # not alerted monsters skip active_work() even if they are in AC_MONSTERS list
        # monsters are alerted when they are attacked/see or hear the player/are "chain-alerted" through other monsters
        self.alert = False
