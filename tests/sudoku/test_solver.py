from argparse import Namespace
from unittest.mock import Mock

import pytest

from sudoku.solver import SudokuSolver, SolveFailedException


class SolverImpl(SudokuSolver):
    def solve_step(self):  # pylint: disable=useless-super-delegation
        return super().solve_step()


@pytest.fixture
def solver(grid):
    return SolverImpl(grid, 3)


class TestSudokuSolver:
    def test_solve_step(self, solver):
        """We're not really testing much here, just want to ensure the method exists."""
        solver.solve_step()

    @pytest.mark.parametrize('mock_complete, mock_solve', (
        ([True], []),
        ([False, False, True], [0, 0]),
        # Check that finding a swap resets the fail counter
        ([False, False, False, False, True], [0, 0, 1, 0, 0]),
    ))
    def test_iter(self, mock_complete, mock_solve, solver):
        solver.grid.is_complete = Mock(side_effect=mock_complete)
        solver.solve_step = Mock(side_effect=mock_solve)
        list(solver)  # Using list() to evaluate the generator until it exits

    def test_iter_failed(self, solver):
        solver.grid.is_complete = Mock(side_effect=[False, False, False])
        with pytest.raises(SolveFailedException):
            list(solver)  # Using list() to evaluate the generator until it fails

    @pytest.mark.parametrize('args, expected', (
        (['web.sud'], Namespace(filename='web.sud', limit=None)),
        (['file.sud', '--limit', '1'], Namespace(filename='file.sud', limit=1)),
    ))
    def test_args(self, args, expected):
        actual = SudokuSolver.args().parse_args(args)
        assert actual == expected

    def test_main(self):
        pass #SudokuSolver.main()
