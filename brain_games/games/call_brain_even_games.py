from brain_games.utils import get_random_int


def is_even(number):
    return True if number % 2 == 0 else False


def generate_round():
    number_to_ask = get_random_int()
    expected_answer = "yes" if is_even(number_to_ask) else "no"
    return [number_to_ask, expected_answer]