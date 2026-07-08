from brain_games.game_engine import game_engine
from brain_games.utils import get_random_int


def is_even(question_part):
    return 'yes' if question_part % 2 == 0 else 'no'


def generate_round():
    min_value = 0
    max_value = 100
    question_part = get_random_int(min_value, max_value)
    return [question_part, is_even(question_part)]


def call_brain_even():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    # call engine
    game_engine(generate_round, description)