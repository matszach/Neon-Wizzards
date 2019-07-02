from src.game_data.entities.characters.character import Character
from src.controllers.views.viewinfo import current_usable_window_space as cws
from util.unit_conversion import cartesian_to_polar
from src.controllers.entity_handlers import pause_unpause
import pygame


# parent class to all player characters
class PlayerCharacter(Character):

    # ===== lifecycle =====
    def active_work(self):

        keys = pygame.key.get_pressed()

        # ===== movement =====
        right = keys[pygame.K_d]
        left = keys[pygame.K_a]
        up = keys[pygame.K_w]
        down = keys[pygame.K_s]

        if right:
            ver = 0
            if up:
                ver -= 45
            if down:
                ver += 45
            self.character_travel(90 + ver)
        elif left:
            ver = 0
            if up:
                ver += 45
            if down:
                ver -= 45
            self.character_travel(270 + ver)
        elif up:
            self.character_travel(0)
        elif down:
            self.character_travel(180)

        # ===== turning =====
        # * assumes player's display location as always in the center of the screen
        loc = pygame.mouse.get_pos()
        mouse_x_from_center = loc[0] - cws[0] - (cws[2])/2
        mouse_y_from_center = loc[1] - cws[1] - (cws[3])/2
        angle, radius = cartesian_to_polar(mouse_x_from_center, mouse_y_from_center)
        self.turn(angle)

        # ===== skills: using =====
        btn = pygame.mouse.get_pressed()

        if btn[0]:
            self.use_chosen_ability()

        # ===== skills: switching =====

        if keys[pygame.K_1]:
            self.switch_to_ability(0)
        elif keys[pygame.K_2]:
            self.switch_to_ability(1)
        elif keys[pygame.K_3]:
            self.switch_to_ability(2)
        elif keys[pygame.K_4]:
            self.switch_to_ability(3)
        elif keys[pygame.K_5]:
            self.switch_to_ability(4)
        elif keys[pygame.K_6]:
            self.switch_to_ability(5)
        elif keys[pygame.K_7]:
            self.switch_to_ability(6)
        elif keys[pygame.K_8]:
            self.switch_to_ability(7)
        elif keys[pygame.K_9]:
            self.switch_to_ability(8)
        elif keys[pygame.K_0]:
            self.switch_to_ability(9)
        elif keys[pygame.K_MINUS]:
            self.switch_to_ability(10)
        elif keys[pygame.K_EQUALS]:
            self.switch_to_ability(11)

    @staticmethod  # todo rethink if this should be here
    def misc_controls():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            pause_unpause()

    # reset on finishing a level
    def prepare_for_next_level(self):
        self.curr_hp = self.max_hp
        self.curr_mp = self.max_mp
        self.has_green_key = False
        self.has_red_key = False
        self.has_blue_key = False
        self.has_boss_key = False

    # constructor
    def __init__(self, sprite_set, display_size=1, collision_size=1, animation_timer=18,
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

        # exp (used for purchasing skills and stat increases between levels)
        self.exp = 0

        # keys
        self.has_green_key = False
        self.has_red_key = False
        self.has_blue_key = False
        self.has_boss_key = False
