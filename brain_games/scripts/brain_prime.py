from brain_games.game_engine import game_engine
from brain_games.games.call_brain_prime_games import generate_round


def main():
    YES_PART = 'Answer "yes" if given number is prime.'
    NO_PART = 'Otherwise answer "no".'
    description = f"{YES_PART} {NO_PART}"
    # call engine
    game_engine(generate_round, description)