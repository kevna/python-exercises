from os import system
from time import sleep
from argparse import ArgumentParser

from life.generation import Generation
from life.game import Game
from life.rule import DEFAULT_RULE, Rule


DEFAULT_DELAY = 0.01


def parse_args():
    """Parse command line arguments with argparse.
    making thise self-contained and separate from functional logic
    means we can safely ignore this from testing.
    """
    parser = ArgumentParser()
    parser.add_argument('width', nargs='?', default=40, type=int)
    parser.add_argument('height', nargs='?', default=20, type=int)
    parser.add_argument('-r', '--rules', default=DEFAULT_RULE, type=Rule)
    parser.add_argument('-d', '--delay', default=DEFAULT_DELAY, type=float)
    return parser.parse_args()

def core_loop(game: Game, delay: float = DEFAULT_DELAY):
    """Perform the game by iterating steps until activity ceases.
    At each generation we clear the screen and display the current generation.
    """
    try:
        for generation in game:
            # Since it takes a moment to render, we do that before clearing to avoid flickering
            display = str(generation)
            system('clear')
            print(display)
            sleep(delay)
    except KeyboardInterrupt:
        pass
    print(f'game ended at generation {game.generations}')

def main():
    """Main method to allow basic terminal interaction
    by specifying the grid size and handling ^C.
    """
    config = parse_args()
    game = Game(Generation.random(config.height, config.width), config.rules)
    core_loop(game, delay=config.delay)


if __name__ == '__main__':
    main()
