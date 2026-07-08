from brain_games.game_engine import game_engine
from brain_games.utils import get_random_int


def is_even(number):
    return True if number % 2 == 0 else False


def generate_round():
    number_to_ask = get_random_int()
    expected_answer = "yes" if is_even(number_to_ask) else "no"
    return [number_to_ask, expected_answer]


def call_brain_even():
    DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
    # call engine
    game_engine(generate_round, DESCRIPTION)