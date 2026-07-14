from brain_games.utils import get_random_int

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_right_answer():
    scope = [5, 10]
    [len, step, start] = [get_random_int(*scope) for _ in range(3)]
    index_to_hide = get_random_int(0, len - 1)
    round_data = ['', '']
    progression = [str(start + index * step) for index in range(len)]
    progression[index_to_hide] = '..'
    round_data[0] = " ".join(progression)
    round_data[1] = str(start + index_to_hide * step)
    return round_data


def prepare():
    return get_question_and_right_answer, DESCRIPTION