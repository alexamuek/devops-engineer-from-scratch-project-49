from brain_games.game_engine import game_engine
from brain_games.games.call_brain_calc_games import generate_round


def main():
    DESCRIPTION = 'What is the result of the expression?'
    # call engine
    game_engine(generate_round, DESCRIPTION)