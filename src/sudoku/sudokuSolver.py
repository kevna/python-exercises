import argparse

from sudokuGrid import SudokuGrid


class SolveFailedException(Exception):
    """Exception for failing to solve the sudoku."""

class SudokuSolver:
    """Abstract class to provide a framework for implementing sudoku solver algorithms."""

    STEPFAILLIMIT = 9

    def __init__(self, filename, fail_limit = STEPFAILLIMIT):
        self.grid = SudokuGrid.load_file(filename)
        self.fail_limit = fail_limit
        self.failed_steps = 0

    def solve_step(self):
        """Perform a single step of solving the sudoku.
        This is intended to be overridden by subclasses to implement
        various methods of solving.
        """
        return False

    def solve(self):
        """Attempt to solve the sudoku.
        This is done by attempting the solve_step implementation repeatedly
        until the limit of consecutive attempts fail to find changes.
        """
        while not self.grid.is_complete():
            if self.solve_step():
                print(self.grid)
                self.failed_steps = 0
            else:
                self.failed_steps += 1
                if self.failed_steps >= self.fail_limit:
                    raise SolveFailedException('Couldn\'t find any more moves toward solution.')

    @staticmethod
    def args():
        """Parse the arguments the solver is called with to prepare to run the solver."""
        parser = argparse.ArgumentParser()
        parser.add_argument('filename', type = str, help = 'name of a sudoku file to solve')
        parser.add_argument('-l', '--limit', type = int, help =
                            'limit attempted steps before solve attempt is counted as failure')
        return parser.parse_args()

    @classmethod
    def main(cls):
        """Run the solver by getting the parsed arguments and triggering the solve loop."""
        args = cls.args()
        solver = cls(args.filename, args.limit)
        try:
            solver.solve()
        except KeyboardInterrupt:
            print('User exit.')
        except SolveFailedException as err:
            print(err)
