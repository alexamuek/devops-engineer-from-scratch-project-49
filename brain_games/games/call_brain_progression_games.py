from brain_games.utils import get_random_int

TASK = 'What number is missing in the progression?'


def get_question_and_right_answer():
    scope = [5, 10]
    [len, step, start] = [get_random_int(*scope) for _ in range(3)]
    index_to_hide = get_random_int(0, len - 1)
    progression = [str(start + index * step) for index in range(len)]
    progression[index_to_hide] = '..'
    task_to_show = " ".join(progression)
    expected_answer = str(start + index_to_hide * step)
    return task_to_show, expected_answer