import numpy as np
from random import random, seed
import src.controllers.states.levelinfo as li

from src.game_data.complete_sets.complete_monsters.cyberzombie import CyberZombie
from src.game_data.complete_sets.complete_monsters.ratling import Ratling

from src.game_data.complete_sets.complete_pickups.crumbs import HealthCrumb, ManaCrumb

from src.controllers import entity_handlers as eh


# main level generator function
def generate_level(level, difficulty, player, level_seed):

    seed(level_seed)

    print(f'LOG: Generating level {level} of difficulty {difficulty}, using seed \"{level_seed}\"')

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
        if not z.check_if_in_wall():
            eh.AC_MONSTERS.append(z)

    for i in range(5):
        r = Ratling()
        r.move_to(5 + random() * 10, 5 + random() * 10)
        if not r.check_if_in_wall():
            eh.AC_MONSTERS.append(r)

    for i in range(20):
        c = HealthCrumb()
        c.move_to(5 + random() * 10, 5 + random() * 10)
        if not c.check_if_in_wall():
            eh.AC_PICKUPS.append(c)

    for i in range(20):
        c = ManaCrumb()
        c.move_to(5 + random() * 10, 5 + random() * 10)
        if not c.check_if_in_wall():
            eh.AC_PICKUPS.append(c)

    #  4 place player
    player.move_to(2, 2)



