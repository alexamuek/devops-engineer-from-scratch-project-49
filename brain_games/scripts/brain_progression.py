from brain_games.game_engine import game_engine
from brain_games.games.call_brain_progression_games import generate_round


def main():
    DESCRIPTION = 'What number is missing in the progression?'
    # call engine
    game_engine(generate_round, DESCRIPTION)