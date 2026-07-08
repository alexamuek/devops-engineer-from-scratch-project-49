from brain_games.game_engine import game_engine
from brain_games.utils import get_random_int


def calculate(number1, number2):
    gcd = 0
    operand1 = number1
    operand2 = number2
    while (abs(operand1 - operand2) >= 0):
        gcd = abs(operand1 - operand2)
        if (gcd == 0):
            break
        else:
            operand2 = min(operand1, operand2)
        operand1 = gcd
    return operand1


def generate_round():
    MIN_VALUE = 1
    [number1, number2] = [get_random_int(min=MIN_VALUE) for _ in range(2)]
    numbers_to_ask = f"{number1} {number2}"
    expected_answer = calculate(number1, number2)
    return [numbers_to_ask, str(expected_answer)]


def call_brain_gcd():
    DESCRIPTION = 'Find the greatest common divisor of given numbers.'
    # call engine
    game_engine(generate_round, DESCRIPTION)