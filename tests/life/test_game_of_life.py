#!/usr/bin/python2
# -*- coding: utf-8 -*-
import pytest

from life.game_of_life import GameOfLife

class TestGameOfLife:
    @pytest.mark.parametrize('grid_arg, row, col, expected', (
        ([
            [False, True , False],
            [False, True , False],
            [False, True , False],
        ], 1, 0, True),
        ([
            [False, False, False],
            [True , True , True ],
            [False, False, False],
        ], 0, 1, True),
        ([
            [False, False, False, False],
            [False, True , True , False],
            [False, True , True , False],
            [False, False, False, False],
        ], 1, 0, False),
        ([
            [False, False, False, False],
            [False, True , True , False],
            [False, True , True , False],
            [False, False, False, False],
        ], 1, 1, True),
        ([
            [False, False, False],
            [True , True , True ],
            [False, False, False],
        ], 0, -1, False),
        #([], 0, 0, False),
    ))
    def test_cell_lives(self, grid_arg, row, col, expected):
        grid = GameOfLife(grid_arg)
        actual = grid.cell_lives(row, col)
        assert actual == expected

    @pytest.mark.parametrize('grid_arg, expected', (
        ([
            [False, True , False],
            [False, True , False],
            [False, True , False],
        ],
        [
            [False, False, False],
            [True , True , True ],
            [False, False, False],
        ]),
        ([
            [False, False, False, False],
            [False, True , True , False],
            [False, True , True , False],
            [False, False, False, False],
        ],
        [
            [False, False, False, False],
            [False, True , True , False],
            [False, True , True , False],
            [False, False, False, False],
        ]),
    ))
    def test_step(self, grid_arg, expected):
        grid = GameOfLife(grid_arg)
        grid.step()
        actual = grid.grid
        assert actual == expected

    @pytest.mark.parametrize('grid_arg, expected', (
        ([
            [False, True , False],
            [False, True , False],
            [False, True , False],
        ], ' \xe2\x96\x88 \n \xe2\x96\x88 \n \xe2\x96\x88 '),
        ([
            [False, False, False],
            [True , True , True ],
            [False, False, False],
        ], '   \n\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n   '),
        ([
            [False, False, False, False],
            [False, True , True , False],
            [False, True , True , False],
            [False, False, False, False],
        ], '    \n \xe2\x96\x88\xe2\x96\x88 \n \xe2\x96\x88\xe2\x96\x88 \n    '),
        #([], 0, 0, False),
    ))
    def test_str(self, grid_arg, expected):
        grid = GameOfLife(grid_arg)
        actual = str(grid)
        assert actual == expected

    @pytest.mark.parametrize('rows, cols, exp_rows, exp_cols', (
        (0, 0, 0, 0),
        (1, 0, 1, 0),
        (10, 10, 10, 10),
        (50, 100, 50, 100),
        (-1, -10, 0, 0),
        #([], 0, 0, False),
    ))
    def test_random_grid(self, rows, cols, exp_rows, exp_cols):
        grid = GameOfLife.random_grid(rows, cols)
        assert len(grid) == exp_rows
        for row in grid:
            assert len(row) == exp_cols
