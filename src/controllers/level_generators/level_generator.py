import numpy as np
from random import random, seed
import src.controllers.states.levelinfo as li

from src.game_data.complete_sets.complete_monsters.cyberzombie import CyberZombie
from src.game_data.complete_sets.complete_monsters.ratling import Ratling

from src.game_data.complete_sets.complete_pickups.crumbs import HealthCrumb, ManaCrumb
from src.game_data.complete_sets.complete_pickups.keys import KeyRed, KeyGreen, KeyBlue, KeyBoss
from src.game_data.complete_sets.complete_obstacles.doors import DoorRed, DoorGreen, DoorBlue, DoorBoss

from src.game_data.complete_sets.complete_obstacles.destroyable_pickup_container import DestroyablePickupContainer

from src.controllers import entity_handlers as eh

from src.controllers.level_generators.room_generator import generate_room_plain


# main level generator function
def generate_level(level, difficulty, player, level_seed):

    seed(level_seed)

    print(f'LOG: Generating level {level} of difficulty {difficulty}, using seed \"{level_seed}\"')

    # TODO implement me
    #  1 generate tile map (0, 1 ,2)
    li.level_fields = np.ones((80, 120), dtype=int)

    for i in range(len(li.level_fields)):
        for j in range(len(li.level_fields[0])):
            if i % 7 == 2 or j % 7 == 2:
                li.level_fields[i][j] = 0

    for i in [10, 20, 30, 40, 60]:
        for j in [10, 20, 30, 40, 60]:
            generate_room_plain(i, j, random()*7+5, random()*7+5, li.level_fields)

    #  2 generate doors and keys

    #  3 generate monsters, obstacles, areas etc.
    for i in range(6):
        z = CyberZombie()
        z.move_to(5+random()*10, 5+random()*10)
        if not z.check_if_in_wall():
            eh.AC_MONSTERS.append(z)

    for i in range(2):
        r = Ratling()
        r.move_to(5 + random() * 10, 5 + random() * 10)
        if not r.check_if_in_wall():
            eh.AC_MONSTERS.append(r)

    for i in range(10):
        c = HealthCrumb()
        c.move_to(5 + random() * 10, 5 + random() * 10)
        if not c.check_if_in_wall():
            eh.AC_PICKUPS.append(c)

    for i in range(10):
        c = ManaCrumb()
        c.move_to(5 + random() * 10, 5 + random() * 10)
        if not c.check_if_in_wall():
            eh.AC_PICKUPS.append(c)

    for i in range(10):
        c = DestroyablePickupContainer(sprite_set_type=int(random()*4))
        c.move_to(5 + random() * 10, 5 + random() * 10)
        if not c.check_if_in_wall():
            eh.AC_OBSTACLES.append(c)
            c.contain(ManaCrumb())
            c.contain(ManaCrumb())
            c.contain(HealthCrumb())
            c.contain(HealthCrumb())

    for k in [KeyRed(), KeyGreen(), KeyBlue(), KeyBoss()]:
        k.move_to(5 + random() * 10, 5 + random() * 10)
        eh.AC_PICKUPS.append(k)
            
    for d in [DoorRed(), DoorGreen(), DoorBlue(), DoorBoss()]:
        d.move_to(5 + random() * 10, 5 + random() * 10)
        eh.AC_OBSTACLES.append(d)

    #  4 place player
    player.move_to(2, 2)



