from brain_games.utils import get_random_int

DESCRIPTION = 'What is the result of the expression?'


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


def get_question_and_right_answer():
    scope = [0] * 2
    OPERATORS = '+-*'
    operator = OPERATORS[get_random_int(max=len(OPERATORS) - 1)]
    match operator:
        case '+':
            scope[0] = 0
            scope[1] = 50
        case '-':
            scope[0] = 0
            scope[1] = 100
        case '*':
            scope[0] = 0
            scope[1] = 10
        case _:
            raise ValueError("Unknown operator")
    [operand1, operand2] = [get_random_int(*scope) for _ in range(2)]
    expression_to_ask = f"{operand1} {operator} {operand2}"
    expected_answer = calculate(operator, operand1, operand2)
    return expression_to_ask, str(expected_answer)


def prepare():
    return get_question_and_right_answer, DESCRIPTION