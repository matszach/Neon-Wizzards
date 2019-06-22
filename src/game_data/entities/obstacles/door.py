from src.game_data.entities.obstacles.obstacle import Obstacle
from random import randint


# parent class to all doors
class Door(Obstacle):

    # ===== lifecycle =====
    def passive_work(self):

        # animate every frame
        self.animate()

        # check open/close conditions
        self.curr_occ_interval += 1
        if self.curr_occ_interval >= self.max_occ_interval:
            self.curr_occ_interval = 0
            if self.check_open_condition():
                self.open()
            elif self.check_close_condition():
                self.close()

    # ===== opening ======
    def check_open_condition(self):
        pass

    def on_open(self):
        pass

    def open(self):
        if self.blocks_movement:
            self.blocks_movement = False
            self.on_open()

    # ===== closing =====
    def check_close_condition(self):
        pass

    def on_close(self):
        pass

    def close(self):
        if not self.blocks_movement:
            self.blocks_movement = True
            self.on_close()

    # constructor
    def __init__(self, sprite_set_open, sprite_set_closed, display_size=1, collision_size=1, animation_timer=15,
                 blocks_movement=True, open_close_check_interval=3):

        # default ("on spawn") sprite set
        sprite_set = sprite_set_closed if blocks_movement else sprite_set_open

        # super constructor
        Obstacle.__init__(self, sprite_set, display_size, collision_size, animation_timer, blocks_movement)

        # alternative spritesets
        self.sprite_set_open = sprite_set_open
        self.sprite_set_closed = sprite_set_closed

        # interval between checking for open / close conditions
        self.max_occ_interval = open_close_check_interval
        self.curr_occ_interval = randint(0, open_close_check_interval)
