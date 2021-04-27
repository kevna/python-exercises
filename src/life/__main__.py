from os import system
from time import sleep
from argparse import ArgumentParser

from life.generation import Generation
from life.game import Game
from life.rule import DEFAULT_RULE, Rule

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('width', nargs='?', default=40, type=int)
    parser.add_argument('height', nargs='?', default=20, type=int)
    parser.add_argument('-r', '--rules', default=DEFAULT_RULE, type=Rule)
    return parser.parse_args()

def core_loop(game: Game):
    """Perform the game by iterating steps until activity ceases.
    At each generation we clear the screen and display the current generation.
    We sleep for 0.1 seconds between each generations.
    """
    try:
        for generation in game:
            system('clear')
            print(generation)
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    print(f'game ended at generation {game.generations}')

def main():
    """Main method to allow basic terminal interaction
    by specifying the grid size and handling ^C.
    """
    config = parse_args()
    game = Game(Generation.random(config.height, config.width), config.rules)
    core_loop(game)


if __name__ == '__main__':
    main()
