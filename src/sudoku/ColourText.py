from enum import Enum


class Colours(Enum):
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


ENDC = '\033[0m'


def colour(text, colour: Colours = Colours.BOLD) -> str:
    return f'{colour.value}{text}{ENDC}'
