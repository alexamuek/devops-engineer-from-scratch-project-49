from brain_games.game_engine import game_engine
from brain_games.utils import get_random_int


def is_even(number):
    return True if number % 2 == 0 else False


def generate_round():
    min_value = 0
    max_value = 100
    question_part = get_random_int(min_value, max_value)
    expected_answer = "yes" if is_even(question_part) else "no"
    return [question_part, expected_answer]


def call_brain_even():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    # call engine
    game_engine(generate_round, description)