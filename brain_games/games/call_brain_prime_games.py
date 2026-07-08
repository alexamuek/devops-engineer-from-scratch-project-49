from brain_games.game_engine import game_engine
from brain_games.utils import get_random_int


def is_prime(number):
    if (number == 1):
        return False
    for divider in range(2, number):
        if (number % divider == 0):
            return False
    return True


def generate_round():
    min_value = 0
    max_value = 100
    question_part = get_random_int(min_value, max_value)
    expected_answer = "yes" if is_prime(question_part) else "no"
    return [question_part, expected_answer]


def call_brain_prime():
    yes_part = 'Answer "yes" if given number is prime.'
    no_part = 'Otherwise answer "no".'
    description = f"{yes_part} {no_part}"
    # call engine
    game_engine(generate_round, description)
