import numpy as np
from random import random
import src.controllers.states.levelinfo as li

from src.game_data.complete_sets.complete_monsters.cyberzombie import CyberZombie
from src.controllers.entity_handlers import AC_MONSTERS


# main level generator function
def generate_level(level, difficulty, player):

    print(f'LOG: Generating level {level} of difficulty {difficulty}.')

    # TODO implement me
    #  1 generate tile map (0, 1 ,2)
    li.level_fields = np.zeros((100, 100), dtype=int)

    for i in range(len(li.level_fields)):
        for j in range(len(li.level_fields[0])):
            if random() > 0.8:
                li.level_fields[i][j] = 1

    #  2 generate doors and keys
    #  3 generate monsters, obstacles, areas etc.
    for i in range(8):
        z = CyberZombie()
        z.move_to(5+random()*10, 5+random()*10)
        AC_MONSTERS.append(z)

    #  4 place player
    player.move_to(2, 2)



