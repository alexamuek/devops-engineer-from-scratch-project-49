from brain_games.games.call_brain_gcd_games import prepare
from brain_games.launch_game import launch_game


def main():
    # call engine
    launch_game(*prepare())


if __name__ == "__main__":
    main()