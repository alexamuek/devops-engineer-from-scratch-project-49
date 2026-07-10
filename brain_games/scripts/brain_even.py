from brain_games.game_engine import game_engine
from brain_games.games.call_brain_even_games import generate_round


def main():
    DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
    # call engine
    game_engine(generate_round, DESCRIPTION)