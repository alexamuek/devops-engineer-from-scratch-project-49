from brain_games.game_engine import game_engine
from brain_games.utils import get_random_int


def generate_round():
    min_value = 5
    max_value = 10
    len = get_random_int(min_value, max_value)
    step = get_random_int(min_value, max_value)
    first_number = get_random_int(min_value, max_value)
    index_to_hide = get_random_int(0, len - 1)
    round_data = ['', '']
    progression = [str(first_number + index * step) for index in range(len)]
    progression[index_to_hide] = '..'
    round_data[0] = " ".join(progression)
    round_data[1] = str(first_number + index_to_hide * step)
    return round_data


def call_brain_progression():
    description = 'What number is missing in the progression?'
    # call engine
    game_engine(generate_round, description)