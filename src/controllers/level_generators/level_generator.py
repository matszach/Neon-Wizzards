import numpy as np
from random import random, seed
import src.controllers.states.levelinfo as li

from src.game_data.complete_sets.complete_monsters.cyberzombie import CyberZombie
from src.game_data.complete_sets.complete_monsters.ratling import Ratling
from src.game_data.complete_sets.complete_monsters.shell_imps import FireShellImp, IceShellImp

from src.game_data.complete_sets.complete_pickups.crumbs import HealthCrumb, ManaCrumb
from src.game_data.complete_sets.complete_pickups.keys import KeyRed, KeyGreen, KeyBlue, KeyBoss
from src.game_data.complete_sets.complete_obstacles.keydoors import DoorRed, DoorGreen, DoorBlue, DoorBoss

from src.game_data.complete_sets.complete_obstacles.destroyable_pickup_container import DestroyablePickupContainer

from src.controllers import entity_handlers as eh

from src.controllers.level_generators.room_generator import generate_room_plain


# main level generator function
def generate_level(level, difficulty, player, level_seed):

    seed(level_seed)

    print(f'LOG: Generating level {level} of difficulty {difficulty}, using seed \"{level_seed}\"')

    # TODO implement me
    #  1 generate tile map (0, 1 ,2)
    li.level_fields = np.ones((100, 100), dtype=int)

    for i in range(len(li.level_fields)):
        for j in range(len(li.level_fields[0])):
            if i % 7 == 2 or j % 7 == 2:
                li.level_fields[i][j] = 0

    for i in [10, 20, 30, 40, 60]:
        for j in [10, 20, 30, 40, 60]:
            generate_room_plain(i, j, random()*7+5, random()*7+5, li.level_fields)

    #  2 generate doors and keys

    #  3 generate monsters, obstacles, areas etc.

    MIN, MAX = 5, 90
    for i in range(30):
        z = CyberZombie()
        z.move_to(MIN+random()*MAX, MIN+random()*MAX)
        if not z.check_if_in_wall():
            eh.AC_MONSTERS.append(z)

    for i in range(10):
        r = Ratling()
        r.move_to(MIN + random() * MAX, MIN + random() * MAX)
        if not r.check_if_in_wall():
            eh.AC_MONSTERS.append(r)

    for i in range(15):
        r = FireShellImp()
        r.move_to(MIN + random() * MAX, MIN + random() * MAX)
        if not r.check_if_in_wall():
            eh.AC_MONSTERS.append(r)

    for i in range(15):
        r = IceShellImp()
        r.move_to(MIN + random() * MAX, MIN + random() * MAX)
        if not r.check_if_in_wall():
            eh.AC_MONSTERS.append(r)

    for i in range(120):
        c = HealthCrumb()
        c.move_to(MIN + random() * MAX, MIN + random() * MAX)
        if not c.check_if_in_wall():
            eh.AC_PICKUPS.append(c)

    for i in range(120):
        c = ManaCrumb()
        c.move_to(MIN + random() * MAX, MIN + random() * MAX)
        if not c.check_if_in_wall():
            eh.AC_PICKUPS.append(c)

    for i in range(100):
        c = DestroyablePickupContainer(sprite_set_type=int(random()*4))
        c.move_to(MIN + random() * MAX, MIN + random() * MAX)
        if not c.check_if_in_wall():
            eh.AC_OBSTACLES.append(c)
            c.contain(ManaCrumb())
            c.contain(ManaCrumb())
            c.contain(HealthCrumb())
            c.contain(HealthCrumb())

    for k in [KeyRed(), KeyGreen(), KeyBlue(), KeyBoss()]:
        k.move_to(MIN + random() * MAX, MIN + random() * MAX)
        eh.AC_PICKUPS.append(k)
            
    for d in [DoorRed(), DoorGreen(), DoorBlue(), DoorBoss()]:
        d.move_to(MIN + random() * MAX, MIN + random() * MAX)
        eh.AC_OBSTACLES.append(d)

    #  4 place player
    player.move_to(2, 2)



