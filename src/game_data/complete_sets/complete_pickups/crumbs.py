from src.game_data.entities.pickups.pickup import Pickup
from random import randint
from src.controllers.views.imginfo import PICKUP_CRUMB_HP, PICKUP_CRUMB_MP, PICKUP_CRUMB_EXP


MIN_VALUE = 2
MAX_VALUE = 5


class HealthCrumb(Pickup):

    # take_effect that picking the pickup up has on the player
    def on_picked_up(self, player):
        player.heal(self.power)

    # constructor
    def __init__(self, slide_direction=0, slide_speed=0):

        # super constructor
        Pickup.__init__(self, PICKUP_CRUMB_HP, display_size=0.4, collision_size=0.2, animation_timer=45,
                        slide_direction=slide_direction, slide_speed=slide_speed)

        # amount of health restored
        self.power = randint(MIN_VALUE, MAX_VALUE)


class ManaCrumb(Pickup):
    # take_effect that picking the pickup up has on the player
    def on_picked_up(self, player):
        player.gain_mp(self.power)

    # constructor
    def __init__(self, slide_direction=0, slide_speed=0):

        # super constructor
        Pickup.__init__(self, PICKUP_CRUMB_MP, display_size=0.4, collision_size=0.2, animation_timer=45,
                        slide_direction=slide_direction, slide_speed=slide_speed)

        # amount of mana restored
        self.power = randint(MIN_VALUE, MAX_VALUE)
