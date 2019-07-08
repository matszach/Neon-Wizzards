from src.game_data.entities.characters.character import Character
from util.unit_conversion import cartesian_to_polar
from src.controllers import entity_handlers as eh
from random import randint


# parent class to all monsters
class Monster(Character):

    # ===== lifecycle =====
    def active_work(self):
        pass

    # ===== player locating =====
    def walk_directly_to_player(self):
        deg = self.get_dir_and_distance_to_player()[0]
        self.character_travel(deg)
        self.turn(deg)

    def sees_player(self):
        player = eh.PLAYER[0]
        x, y = player.x, player.y
        return self.sees_location(x, y, self.sight_range)

    def get_dir_and_distance_to_player(self):
        player = eh.PLAYER[0]
        x_dir = player.x - self.x
        y_dir = player.y - self.y
        return cartesian_to_polar(x_dir, y_dir)

    # constructor
    def __init__(self, sprite_set, display_size=1, collision_size=1, animation_timer=15,
                 hp=100, physical_def=0, fire_def=0, cold_def=0, lightning_def=0,
                 holy_def=0, shadow_def=0, acid_def=0,
                 mp=100, speed=0.02, strength=5, dexterity=5, intelligence=5, flying=False,
                 dif_mod=1, pathing_increment=30, sight_range=10):

        # super constructors
        Character.__init__(self, sprite_set, display_size, collision_size, animation_timer,
                           hp * dif_mod, physical_def, fire_def, cold_def, lightning_def,
                           holy_def, shadow_def, acid_def,
                           mp, speed, strength, dexterity, intelligence, flying)

        # how often the monster checks for path
        self.max_pathing_increment = pathing_increment
        self.curr_pathing_increment = randint(0, pathing_increment)

        # current direction of movement (possibly ignored when in direct sight of the player)
        # TODO might not be needed
        self.path_dir = 0

        # not alerted monsters skip active_work() even if they are in AC_MONSTERS list
        # monsters are alerted when they are attacked/see or hear the player/are "chain-alerted" through other monsters
        self.alert = False

        # sight / alert range
        self.sight_range = sight_range
