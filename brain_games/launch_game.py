import prompt

from .cli import welcome_user


def launch_game(get_round_data, description):
    name = welcome_user()
    print(description)
    ROUNDS = 3
    for _ in range(ROUNDS):
        round_data = get_round_data()
        print(f"Question: {round_data[0]}")
        answer = prompt.string('Your answer: ')
        if (answer.lower() == round_data[1]):
            print('Correct!')
        else:
            correct_part = f"Correct answer was '{round_data[1]}'"
            print(f"'{answer}' is wrong answer ;(. {correct_part}")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")