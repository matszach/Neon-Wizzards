from src.controllers.views.painter import paint_entity, paint_monster, paint_player

"""
holds player at 0th index,
list used for its immutability (?)
"""
PLAYER = []

"""
active entities in their draw order
"""
AC_AREAS = []
AC_OBSTACLES = []
AC_PICKUPS = []
AC_CORPSES = []
AC_SUMMONINGS = []

AC_MONSTERS = []

AC_ALLIES = []
AC_PARTICLES = []
AC_PROJECTILES = []

"""
dormant entities and their "activation" range
"""
DR_OBSTACLES = []
MAX_RANGE_OBSTACLES_X = 18
MAX_RANGE_OBSTACLES_Y = 11
DR_PICKUPS = []
MAX_RANGE_PICKUPS_X = 18
MAX_RANGE_PICKUPS_y = 11
DR_MONSTERS = []
MAX_RANGE_MONSTERS_X = 25
MAX_RANGE_MONSTERS_Y = 16


"""

"""


def reset():
    pass


"""

"""


def adjust_active():
    cull_entity_group(AC_MONSTERS, DR_MONSTERS, MAX_RANGE_MONSTERS_X, MAX_RANGE_MONSTERS_Y)
    cull_entity_group(AC_OBSTACLES, DR_OBSTACLES, MAX_RANGE_OBSTACLES_X, MAX_RANGE_OBSTACLES_Y)
    cull_entity_group(AC_PICKUPS, DR_PICKUPS, MAX_RANGE_PICKUPS_X, MAX_RANGE_PICKUPS_y)


def cull_entity_group(active, dormant, mrange_x, mrange_y):
    for e in dormant:
        if abs(e.x - PLAYER[0].x) < mrange_x or abs(e.y - PLAYER[0].y) < mrange_y:
            dormant.remove(e)
            active.append(e)
    for e in active:
        if abs(e.x - PLAYER[0].x) > mrange_x or abs(e.y - PLAYER[0].y) > mrange_y:
            dormant.append(e)
            active.remove(e)


"""

"""

CULL_INCREMENT = 120
cull_timer = [0]


def handle_all():

    # "under-characters" entities
    for entity_set in [AC_AREAS, AC_OBSTACLES, AC_PICKUPS, AC_CORPSES, AC_SUMMONINGS]:
        for e in entity_set:
            e.passive_work()
            paint_entity(e)

    # characters
    for m in AC_MONSTERS:
        m.passive_work()
        m.active_work()
        paint_monster(m)

    # PLAYER[0].passive_work()
    # PLAYER[0].active_work()
    # paint_player(PLAYER[0])

    # "over-characters" entities
    for entity_set in [AC_AREAS, AC_OBSTACLES, AC_PICKUPS, AC_CORPSES, AC_SUMMONINGS]:
        for e in entity_set:
            e.passive_work()
            paint_entity(e)

    # active/dormant culling
    if cull_timer[0] >= CULL_INCREMENT:
        adjust_active()
        cull_timer[0] = 0
    cull_timer[0] += 1


"""

"""


def paint_all():

    # "under-characters" entities
    for entity_set in [AC_AREAS, AC_OBSTACLES, AC_PICKUPS, AC_CORPSES, AC_SUMMONINGS]:
        for e in entity_set:
            paint_entity(e)

    # characters
    for m in AC_MONSTERS:
        paint_monster(m)

    # paint_player(PLAYER[0])

    # "over-characters" entities
    for entity_set in [AC_AREAS, AC_OBSTACLES, AC_PICKUPS, AC_CORPSES, AC_SUMMONINGS]:
        for e in entity_set:
            paint_entity(e)

