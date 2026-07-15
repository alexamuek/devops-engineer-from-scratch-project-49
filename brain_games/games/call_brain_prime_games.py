from brain_games.utils import get_random_int

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if (number <= 1):
        return False
    for divisor in range(2, number):
        if (number % divisor == 0):
            return False
    return True


def get_question_and_right_answer():
    number_to_ask = get_random_int()
    expected_answer = "yes" if is_prime(number_to_ask) else "no"
    return number_to_ask, expected_answer
