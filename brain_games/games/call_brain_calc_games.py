from brain_games.game_engine import game_engine
from brain_games.utils import get_random_int


def calculate(operator, number1, number2):
    match operator:
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case '*':
            return number1 * number2
        case _:
            raise ValueError("Unknown operator")
    return 0


def generate_round():
    number_boundaries = [0] * 2
    operators = '+-*'
    operator = operators[get_random_int(0, len(operators) - 1)]
    match operator:
        case '+':
            number_boundaries[0] = 0
            number_boundaries[1] = 50
        case '-':
            number_boundaries[0] = 0
            number_boundaries[1] = 100
        case '*':
            number_boundaries[0] = 0
            number_boundaries[1] = 10
        case _:
            raise ValueError("Unknown operator")
    first_operand = get_random_int(number_boundaries[0], number_boundaries[1])
    second_operand = get_random_int(number_boundaries[0], number_boundaries[1])
    expression = f"{first_operand} {operator} {second_operand}"
    answer = calculate(operator, first_operand, second_operand)
    return [expression, str(answer)]


def call_brain_calc():
    description = 'What is the result of the expression?'
    # call engine
    game_engine(generate_round, description)