import src.game_data.complete_sets.complete_player_characters.estera.skills.level_1_skills as lev_1

"""
Each player character will have "skill trees"
learning new skill (of given level and number)
triggers an effect, be it stat alteration or gaining an ability)
"""


def get_talent(level, i, player):

    # raise exception if illegal player passed
    from src.game_data.complete_sets.complete_player_characters.estera.pc_estera import PlayerCharacterEstera
    if not isinstance(player, PlayerCharacterEstera):
        raise Exception(f'IllegalPlayerClassException: {player} is not an instance of {PlayerCharacterEstera}.')

    # Log
    print(f'LOG: Estera learns skill {i} of {level}. level.')

    if level == 1:
        lev_1.gain_skill(player, i)

    # TODO complete me
