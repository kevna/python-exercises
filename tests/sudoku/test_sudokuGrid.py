#!/usr/bin/python2
# -*- coding: utf-8 -*-
import pytest

from sudoku.sudokuGrid import SudokuGrid


class TestSudokuGrid:
    @pytest.mark.parametrize('grid_arg, arg_row, arg_number, exp_possibilities', (
        #([], True),
        #([[]], True),
        #([
        #    [1, 2, 3, 4, 5, 6, 7, 8, 9],
        #], True),
        #([
        #    [1, 2, 3, 4, None, 6, 7, 8, 9],
        #], False),
        #(-1, None),
    ))
    def test_row_remove_possibility(self, grid_arg, arg_row, arg_number, exp_possibilities):
        grid = SudokuGrid(grid_arg)
        grid.row_remove_possibility(arg_row, arg_number)
        for exp_key in exp_possibilities:
            expected = exp_possibilities[exp_key]
            actual = grid.grid[0][exp_key]
            assert actual == expected

    @pytest.mark.parametrize('grid_arg, expected', (
        ([], True),
        ([[]], True),
        ([
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
        ], True),
        ([
            [1, 2, 3, 4, None, 6, 7, 8, 9],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
        ], False),
        #(-1, None),
    ))
    def test_is_complete(self, grid_arg, expected):
        grid = SudokuGrid(grid_arg)
        actual = grid.is_complete()
        assert actual == expected

    @pytest.mark.parametrize('grid1_arg, grid2_arg, expected', (
        #([], [], True),
        #([[]], [[]], True),
        ([
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
        ],
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
        ], True),
        ([
            [1, 2, 3, 4, None, 6, 7, 8, 9],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
        ],
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
        ], False),
        ([
            [1, 2, 3, 4, None, 6, 7, 8, 9],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
        ],
        [
            [1, 2, 3, 4, None, 6, 7, 8, 9],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
        ], True),
        ([
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
        ],
        [
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
        ], True),
        #(-1, None),
    ))
    def test_eq(self, grid1_arg, grid2_arg, expected):
        grid1 = SudokuGrid(grid1_arg)
        grid2 = SudokuGrid(grid2_arg)
        actual = grid1 == grid2
        assert actual == expected

    @pytest.mark.parametrize('grid_arg, expected', (
        ([], '|'),
        ([[]], '|\n|\n|'),
        (
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [2, 3, 4, 5, 6, 7, 8, 9, 1],
            ],
            '|-------|-------|-------|\n'
            '| 1 2 3 | 4 5 6 | 7 8 9 |\n'
            '| 2 3 4 | 5 6 7 | 8 9 1 |\n'
            '|-------|-------|-------|'
        ),
        #(-1, None),
    ))
    def test_str(self, grid_arg, expected):
        grid = SudokuGrid(grid_arg)
        actual = str(grid)
        assert actual == expected
