from random import randint
from src.controllers import entity_handlers as eh


class PickupDropping:

    def drop_all_items(self):
        for p in self.pickups_held:
            p.slide_speed = 0.07
            p.slide_direction = randint(0, 360)
            p.move_to(self.x, self.y)
            eh.AC_PICKUPS.append(p)
        self.pickups_held.clear()

    def contain(self, pickup):
        self.pickups_held.append(pickup)

    # constructor
    def __init__(self):

        # list of held pickup entities
        self.pickups_held = []
