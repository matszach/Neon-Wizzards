from src.game_data.entities.pickups.pickup import Pickup
from src.controllers.views.imginfo import PICKUP_KEY_RED, PICKUP_KEY_GREEN, PICKUP_KEY_BLUE, PICKUP_KEY_BOSS

DISP_SIZE = 1
COL_SIZE = 1
ANIM_TIMER = 45


class KeyRed(Pickup):

    def on_picked_up(self, player):
        player.has_red_key = True

    def __init__(self):
        Pickup.__init__(self, PICKUP_KEY_RED, DISP_SIZE, COL_SIZE, ANIM_TIMER)


class KeyGreen(Pickup):

    def on_picked_up(self, player):
        player.has_green_key = True

    def __init__(self):
        Pickup.__init__(self, PICKUP_KEY_GREEN, DISP_SIZE, COL_SIZE, ANIM_TIMER)


class KeyBlue(Pickup):

    def on_picked_up(self, player):
        player.has_blue_key = True

    def __init__(self):
        Pickup.__init__(self, PICKUP_KEY_BLUE, DISP_SIZE, COL_SIZE, ANIM_TIMER)


class KeyBoss(Pickup):

    def on_picked_up(self, player):
        player.has_boss_key = True

    def __init__(self):
        Pickup.__init__(self, PICKUP_KEY_BOSS, DISP_SIZE, COL_SIZE, ANIM_TIMER)


