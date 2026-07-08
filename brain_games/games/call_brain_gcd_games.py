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
    min_value = 1
    max_value = 100
    number1 = get_random_int(min_value, max_value)
    number2 = get_random_int(min_value, max_value)
    question_part = f"{number1} {number2}"
    answer = calculate(number1, number2)
    return [question_part, str(answer)]


def call_brain_gcd():
    description = 'Find the greatest common divisor of given numbers.'
    # call engine
    game_engine(generate_round, description)