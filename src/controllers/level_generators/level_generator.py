import numpy as np
from random import randint, random
import src.controllers.states.levelinfo as li


# main level generator function
def generate_level(level, difficulty, player):

    print(f'LOG: Generating level {level} of difficulty {difficulty}.')

    # TODO implement me
    #  1 generate tile map (0, 1 ,2)
    li.level_fields = np.zeros((100, 100), dtype=int)

    for i in range(len(li.level_fields)):
        for j in range(len(li.level_fields[0])):
            if random() > 0.75:
                li.level_fields[i][j] = 1

    #  2 generate doors and keys
    #  3 generate monsters, obstacles, areas etc.
    #  4 place player
