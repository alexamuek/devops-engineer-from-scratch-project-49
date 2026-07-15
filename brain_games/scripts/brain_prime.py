from brain_games.games.call_brain_prime_games import (
    TASK,
    get_question_and_right_answer,
)
from brain_games.launch_game import launch_game


def main():
    # call engine
    launch_game(get_question_and_right_answer, TASK)


if __name__ == "__main__":
    main()