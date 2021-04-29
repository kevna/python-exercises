import pytest

from sudoku.grid import SudokuGrid
from sudoku.simple_solver import SimpleSudokuSolver


@pytest.fixture
def solver(grid):
    return SimpleSudokuSolver(grid)


class TestSimpleSudokuSolver:
    @pytest.mark.parametrize('original, expected', (
        (
            [
                [None, None, 4, 9, None, 2, None, None, 1],
                [None, 6, 2, None, None, None, 7, 3, None],
                [5, None, None, None, None, None, None, None, None],
                [None, None, 8, 7, 4, None, 6, None, None],
                [6, None, None, None, None, None, None, None, 7],
                [None, None, 5, None, 3, 6, 1, None, None],
                [None, None, None, None, None, None, None, None, 6],
                [None, 7, 6, None, None, None, 8, 1, None],
                [9, None, None, 2, None, 1, 4, None, None],
            ],
            [
                [None, None, 4, 9, None, 2, 5, None, 1],
                [None, 6, 2, None, None, None, 7, 3, None],
                [5, None, None, None, None, None, None, None, None],
                [None, None, 8, 7, 4, None, 6, None, None],
                [6, None, None, None, None, None, None, None, 7],
                [None, None, 5, 8, 3, 6, 1, None, None],
                [None, None, None, None, None, None, None, None, 6],
                [None, 7, 6, None, None, None, 8, 1, None],
                [9, None, 3, 2, None, 1, 4, None, None],
            ],
        ),
    ))
    def test_solve_step(self, original, expected):
        solver = SimpleSudokuSolver(SudokuGrid(original))
        solver.solve_step()
        actual = [[cell.value for cell in row] for row in solver.grid._grid]
        assert actual == expected
