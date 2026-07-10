from brain_games.game_engine import game_engine
from brain_games.games.call_brain_gcd_games import generate_round


def main():
    DESCRIPTION = 'Find the greatest common divisor of given numbers.'
    # call engine
    game_engine(generate_round, DESCRIPTION)