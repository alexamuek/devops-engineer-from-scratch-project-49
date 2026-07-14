from brain_games.utils import get_random_int

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return True if number % 2 == 0 else False


def get_question_and_right_answer():
    number_to_ask = get_random_int()
    expected_answer = "yes" if is_even(number_to_ask) else "no"
    return number_to_ask, expected_answer


def prepare():
    return get_question_and_right_answer, DESCRIPTION