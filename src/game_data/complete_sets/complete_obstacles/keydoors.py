from src.game_data.entities.obstacles.door import Door
from src.controllers.views.imginfo import OBSTACLE_DOOR_RED, OBSTACLE_DOOR_GREEN, \
    OBSTACLE_DOOR_BLUE, OBSTACLE_DOOR_BOSS, OBSTACLE_DOOR_OPEN

from src.controllers import entity_handlers as eh

DIST_TO_PLAYER = 1


class DoorRed(Door):

    def check_close_condition(self):
        return False

    def check_open_condition(self):
        player = eh.PLAYER[0]
        if (abs(player.x-self.x) + abs(player.y-self.y))/2 > DIST_TO_PLAYER:
            return False
        return player.has_red_key

    def on_open(self):
        pass
        # TODO animation

    def __init__(self):
        Door.__init__(self, OBSTACLE_DOOR_OPEN, OBSTACLE_DOOR_RED)


class DoorGreen(Door):

    def check_close_condition(self):
        return False

    def check_open_condition(self):
        player = eh.PLAYER[0]
        if (abs(player.x - self.x) + abs(player.y - self.y)) / 2 > DIST_TO_PLAYER:
            return False
        return player.has_green_key

    def on_open(self):
        pass
        # TODO animation

    def __init__(self):
        Door.__init__(self, OBSTACLE_DOOR_OPEN, OBSTACLE_DOOR_GREEN)


class DoorBlue(Door):

    def check_close_condition(self):
        return False

    def check_open_condition(self):
        player = eh.PLAYER[0]
        if (abs(player.x - self.x) + abs(player.y - self.y)) / 2 > DIST_TO_PLAYER:
            return False
        return player.has_blue_key

    def on_open(self):
        pass
        # TODO animation

    def __init__(self):
        Door.__init__(self, OBSTACLE_DOOR_OPEN, OBSTACLE_DOOR_BLUE)


class DoorBoss(Door):

    def check_close_condition(self):
        return False

    def check_open_condition(self):
        player = eh.PLAYER[0]
        if (abs(player.x - self.x) + abs(player.y - self.y)) / 2 > DIST_TO_PLAYER:
            return False
        return player.has_boss_key

    def on_open(self):
        pass
        # TODO animation

    def __init__(self):
        Door.__init__(self, OBSTACLE_DOOR_OPEN, OBSTACLE_DOOR_BOSS)
