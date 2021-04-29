#!/usr/bin/python2
# -*- coding: utf-8 -*-
from itertools import zip_longest
from unittest.mock import patch, call

from ansi.colour import fg, fx  # type: ignore
import pytest

from sudoku.grid import SudokuGrid


class TestSudokuGrid:
    @pytest.mark.parametrize('filename, file, expected', (
        (
            'noextension',
            ['', '', '', '', '', '', '', '', ''],
            []
        ),
        (
            'dumb.sudoku',
            [
                '123456789',
                '234567891',
                '345678912',
                '456789123',
                '567891234',
                '678912345',
                '789123456',
                '891234567',
                '912345678',
            ],
            []
        ),
    ))
    @patch('sudoku.grid.open')
    def test_load_file(self, mock_open, filename, file, expected):
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.readline.side_effect = file
        actual = SudokuGrid.load_file(filename)
        assert mock_open.call_args == call(filename)
        # TODO assert actual == expected

    @pytest.mark.parametrize('coords, expected', (
        ((0, 0), (0, 0)),
        ((8, 8), (6, 6)),
        ((5, 8), (3, 6)),
        ((5, 2), (3, 0)),
    ))
    def test_get_box_coords(self, coords, expected, grid):
        actual = grid.get_box_coords(*coords)
        assert actual == expected

    @pytest.mark.parametrize('row, expected', (
        ([], True),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            True,
        ),
        (
            [1, 2, 3, 4, None, 6, 7, 8, 9],
            False,
        ),
    ))
    def test_row_complete(self, row, expected):
        grid = SudokuGrid([row])
        actual = grid.row_complete(0)
        assert actual is expected

    def test_row_complete_stored(self):
        grid = SudokuGrid([[None]])
        grid._complete_rows = [0]
        actual = grid.row_complete(0)
        assert actual is True

    @pytest.mark.parametrize('col, expected', (
        ([], True),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            True,
        ),
        (
            [1, 2, 3, 4, None, 6, 7, 8, 9],
            False,
        ),
    ))
    def test_col_complete(self, col, expected):
        grid = SudokuGrid([[row] for row in col])
        actual = grid.col_complete(0)
        assert actual is expected

    def test_col_complete_stored(self):
        grid = SudokuGrid([[None]])
        grid._complete_cols = [0]
        actual = grid.col_complete(0)
        assert actual is True

    @pytest.mark.parametrize('box, expected', (
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            True,
        ),
        (
            [
                [1, 2, 3],
                [4, None, 6],
                [7, 8, 9],
            ],
            False,
        ),
    ))
    def test_box_complete(self, box, expected):
        grid = SudokuGrid(box)
        actual = grid.box_complete(0, 0)
        assert actual is expected

    def test_box_complete_stored(self):
        grid = SudokuGrid([[None]])
        grid._complete_boxes = [(0, 0)]
        actual = grid.box_complete(0, 0)
        assert actual is True

    @pytest.mark.parametrize('box, expected', (
        (
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
            ],
            True,
        ),
        (
            [
                [1, None],
                [2, None],
                [3, None],
                [4, None],
                [5, None],
                [6, None],
                [7, None],
                [8, None],
                [9, None],
            ],
            True,
        ),
        (
            [
                [1, 2, 3, None],
                [4, 5, 6, None],
                [7, 8, 9, None],
                [None, None, None, None],
            ],
            True,
        ),
        (
            [
                [1, 2, 3, None],
                [4, None, 6, None],
                [7, 8, 9, None],
                [None, None, None, None],
            ],
            False,
        ),
    ))
    def test_cell_complete(self, box, expected):
        grid = SudokuGrid(box)
        actual = grid.cell_complete(0, 0)
        assert actual is expected

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
        assert actual is expected

    def test_eq_type(self, grid):
        actual = grid == None
        assert actual is False

    hl = fg.green + fx.crossed_out
    b = fx.bold
    r = fx.reset
    hlb = f'{r}{hl}{b}'
    @pytest.mark.parametrize('grid_arg, expected', (
        (
            [],
            '┼───────┼───────┼───────┼\n'
            'Total Found: 0\nRemaining Possibilities: 0'
        ),
        (
            [[]],
            '┼───────┼───────┼───────┼\n'
            '│\n'
            '┼───────┼───────┼───────┼\n'
            'Total Found: 0\nRemaining Possibilities: 0'
        ),
        (
            [
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [2, 3, 4, 5, 6, 7, 8, 9, 1],
            ],
            '┼───────┼───────┼───────┼\n'
            f'│{hl} {hlb}1{r}{r}{hl} {hlb}2{r}{r}{hl} {hlb}3{r}{r}{hl} {r}│'
                f'{hl} {hlb}4{r}{r}{hl} {hlb}5{r}{r}{hl} {hlb}6{r}{r}{hl} {r}│'
                f'{hl} {hlb}7{r}{r}{hl} {hlb}8{r}{r}{hl} {hlb}9{r}{r}{hl} {r}│\n'
            f'│{hl} {hlb}2{r}{r}{hl} {hlb}3{r}{r}{hl} {hlb}4{r}{r}{hl} {r}│'
                f'{hl} {hlb}5{r}{r}{hl} {hlb}6{r}{r}{hl} {hlb}7{r}{r}{hl} {r}│'
                f'{hl} {hlb}8{r}{r}{hl} {hlb}9{r}{r}{hl} {hlb}1{r}{r}{hl} {r}│\n'
            '┼───────┼───────┼───────┼\n'
            'Total Found: 18\n'
            'Remaining Possibilities: 0'
        ),
    ))
    def test_str(self, grid_arg, expected):
        grid = SudokuGrid(grid_arg)
        actual = str(grid)
        assert actual == expected

    def test_len(self, grid):
        assert len(grid) == len(grid._grid)

    def test_getitem(self, grid):
        assert grid[0] == grid._grid[0]

    def test_iter(self, grid):
        for item, _item in zip_longest(grid, grid._grid):
            assert item == _item
