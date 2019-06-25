from src.game_data.entities.characters.character import Character


# parent class to all player characters
class PlayerCharacter(Character):

    # ===== lifecycle =====
    def active_work(self):
        # TODO user input handling here
        pass

    # reset on finishing a level
    def prepare_for_next_level(self):
        self.curr_hp = self.max_hp
        self.curr_mp = self.max_mp
        self.has_green_key = False
        self.has_red_key = False
        self.has_blue_key = False
        self.has_boss_key = False

    # constructor
    def __init__(self, sprite_set, display_size=1, collision_size=1, animation_timer=15,
                 hp=100, physical_def=0, fire_def=0, cold_def=0, lightning_def=0,
                 holy_def=0, shadow_def=0, acid_def=0,
                 mp=100, speed=0.1, strength=5, dexterity=5, intelligence=5, flying=False):

        # super constructors
        Character.__init__(self, sprite_set, display_size, collision_size, animation_timer,
                           hp, physical_def, fire_def, cold_def, lightning_def,
                           holy_def, shadow_def, acid_def,
                           mp, speed, strength, dexterity, intelligence, flying)

        # score (may not be used)
        self.score = 0

        # exp (used for purchasing abilities and stat increases between levels)
        self.exp = 0

        # keys
        self.has_green_key = False
        self.has_red_key = False
        self.has_blue_key = False
        self.has_boss_key = False
