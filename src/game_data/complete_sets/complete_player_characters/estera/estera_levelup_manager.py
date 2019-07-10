import src.game_data.complete_sets.complete_player_characters.estera.skills.level_1_skills as lev_1
import src.game_data.complete_sets.complete_player_characters.estera.skills.level_2_skills as lev_2
import src.game_data.complete_sets.complete_player_characters.estera.skills.level_3_skills as lev_3
import src.game_data.complete_sets.complete_player_characters.estera.skills.level_4_skills as lev_4
import src.game_data.complete_sets.complete_player_characters.estera.skills.level_5_skills as lev_5


"""
Each player character will have "skill trees"
learning new skill (of given level and number)
triggers an effect, be it stat alteration or gaining an ability)
"""

# will be referenced by level up view
KNOWN_SKILLS = [
    [0, 0, 0, 0, 0],  # 1 lvl
    [0, 0, 0, 0, 0],  # 2 lvl
    [0, 0, 0, 0, 0],  # 3 lvl
    [0, 0, 0, 0, 0],  # 4 lvl
    [0, 0, 0, 0, 0]   # 5 lvl
]


def reset():
    for i in range(len(KNOWN_SKILLS)):
        KNOWN_SKILLS[i] = [0, 0, 0, 0, 0]


def get_talent(level, i, player):

    # raise exception if illegal player passed
    from src.game_data.complete_sets.complete_player_characters.estera.pc_estera import PlayerCharacterEstera
    if not isinstance(player, PlayerCharacterEstera):
        raise Exception(f'IllegalPlayerClassException: {player} is not an instance of {PlayerCharacterEstera}.')

    if KNOWN_SKILLS[level][i]:
        print(f'LOG: Estera already knows skill {i} of {level}. level.')
        return

    if level == 1:
        lev_1.gain_skill(player, i)
    elif level == 2:
        lev_2.gain_skill(player, i)
    elif level == 3:
        lev_3.gain_skill(player, i)
    elif level == 4:
        lev_4.gain_skill(player, i)
    elif level == 5:
        lev_5.gain_skill(player, i)

    # Log
    print(f'LOG: Estera learns skill {i} of {level}. level.')
    KNOWN_SKILLS[level][i] = 1
