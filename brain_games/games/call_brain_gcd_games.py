from brain_games.utils import get_random_int

TASK = 'Find the greatest common divisor of given numbers.'


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


def get_question_and_right_answer():
    MIN_VALUE = 1
    [number1, number2] = [get_random_int(min=MIN_VALUE) for _ in range(2)]
    numbers_to_ask = f"{number1} {number2}"
    expected_answer = calculate(number1, number2)
    return numbers_to_ask, str(expected_answer)