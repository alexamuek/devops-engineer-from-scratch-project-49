from brain_games.game_engine import game_engine
from brain_games.utils import get_random_int


def is_prime(number):
    if (number == 1):
        return False
    for divisor in range(2, number):
        if (number % divisor == 0):
            return False
    return True


def generate_round():
    number_to_ask = get_random_int()
    expected_answer = "yes" if is_prime(number_to_ask) else "no"
    return [number_to_ask, expected_answer]


def call_brain_prime():
    YES_PART = 'Answer "yes" if given number is prime.'
    NO_PART = 'Otherwise answer "no".'
    description = f"{YES_PART} {NO_PART}"
    # call engine
    game_engine(generate_round, description)
