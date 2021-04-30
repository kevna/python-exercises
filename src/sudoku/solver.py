from abc import ABC, abstractmethod
from argparse import ArgumentParser
from typing import Optional

from sudoku.grid import SudokuGrid


class SolveFailedException(Exception):
    """Exception for failing to solve the sudoku."""

class SudokuSolver(ABC):
    """Abstract class to provide a framework for implementing sudoku solver algorithms."""

    STEPFAILLIMIT = 9

    def __init__(self, grid: SudokuGrid, fail_limit: int = None):
        self.grid = grid
        self.fail_limit = fail_limit or self.STEPFAILLIMIT
        self.failed_steps = 0

    @abstractmethod
    def solve_step(self) -> int:
        """Perform a single step of solving the sudoku.
        This is intended to be overridden by subclasses to implement
        various methods of solving.
        """
        return 0

    def __iter__(self):
        """Attempt to solve the sudoku.
        This is done by attempting the solve_step implementation repeatedly
        until the limit of consecutive attempts fail to find changes.
        """
        while not self.grid.is_complete():
            if self.solve_step():
                self.failed_steps = 0
                yield self.grid
            else:
                self.failed_steps += 1
                if self.failed_steps >= self.fail_limit:
                    raise SolveFailedException('Couldn\'t find any more moves toward solution.')

    @staticmethod
    def args(parser: Optional[ArgumentParser] = None) -> ArgumentParser:
        """Parse the arguments the solver is called with to prepare to run the solver."""
        if not parser:
            parser = ArgumentParser()
        parser.add_argument('filename', type = str, help = 'name of a sudoku file to solve')
        parser.add_argument('-l', '--limit', type = int, help =
                            'limit attempted steps before solve attempt is counted as failure')
        return parser

    @classmethod
    def main(cls):
        """Run the solver by getting the parsed arguments and triggering the solve loop."""
        args = cls.args().parse_args()
        solver = cls(
            SudokuGrid.load_file(args.filename),
            args.limit
        )
        try:
            for grid in solver:
                print(grid)
        except KeyboardInterrupt:
            print('User exit.')
        except SolveFailedException as err:
            print(err)
