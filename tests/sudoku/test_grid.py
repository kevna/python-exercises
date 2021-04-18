#!/usr/bin/python2
# -*- coding: utf-8 -*-
import pytest

from sudoku.grid import SudokuGrid


class TestSudokuGrid:
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
    ))
    def test_is_complete(self, grid_arg, expected):
        grid = SudokuGrid(grid_arg)
        actual = grid.is_complete()
        assert actual == expected

    @pytest.mark.parametrize('grid1_arg, grid2_arg, expected', (
        ([], [], True),
        ([[]], [[]], True),
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
    ))
    def test_eq(self, grid1_arg, grid2_arg, expected):
        grid1 = SudokuGrid(grid1_arg)
        grid2 = SudokuGrid(grid2_arg)
        actual = grid1 == grid2
        assert actual == expected

    @pytest.mark.parametrize('grid_arg, expected', (
        ([], '┼\nTotal Found: 0\nRemaining Possibilities: 0'),
        ([[]], '┼\n\x1b[95m│\x1b[0m\n┼\nTotal Found: 0\nRemaining Possibilities: 0'),
        #(
        #    [
        #        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        #        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        #    ],
        #    '┼───────┼───────┼───────┼\n'
        #    '│ 1 2 3 │ 4 5 6 │ 7 8 9 │\n'
        #    '│ 2 3 4 │ 5 6 7 │ 8 9 1 │\n'
        #    '┼───────┼───────┼───────┼\n'
        #    'Total Found: 18\n'
        #    'Remaining Possibilities: 0'
        #),
    ))
    def test_str(self, grid_arg, expected):
        grid = SudokuGrid(grid_arg)
        actual = str(grid)
        assert actual == expected
