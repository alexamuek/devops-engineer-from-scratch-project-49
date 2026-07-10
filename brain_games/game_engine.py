import prompt

from .cli import welcome_user


def game_engine(generate_round, description):
    name = welcome_user()
    print(f"Hello, {name}!")
    print(description)
    ROUNDS = 3
    for _ in range(ROUNDS):
        round_data = generate_round()
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