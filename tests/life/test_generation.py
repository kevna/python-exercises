#!/usr/bin/python2
# -*- coding: utf-8 -*-
import pytest

from life.generation import Generation


class TestGeneration:
    @pytest.mark.parametrize('height, width, exp_rows, exp_cols', (
        (0, 0, 0, 0),
        (1, 0, 1, 0),
        (10, 10, 10, 10),
        (50, 100, 50, 100),
        (-1, -10, 0, 0),
    ))
    def test_random_grid(self, height, width, exp_rows, exp_cols):
        gen = Generation.random(height, width)
        assert len(gen._grid) == exp_rows
        for row in gen._grid:
            assert len(row) == exp_cols

    @pytest.mark.parametrize('grid, row, col, expected', (
        (
            [
                [False, True , False],
                [False, True , False],
                [False, True , False],
            ],
            1, 0,
            3,
        ),
        (
            [
                [False, False, False],
                [True , True , True ],
                [False, False, False],
            ],
            0, 1,
            3,
        ),
        (
            [
                [False, False, False, False],
                [False, True , True , False],
                [False, True , True , False],
                [False, False, False, False],
            ],
            1, 0,
            2,
        ),
        (
            [
                [False, False, False, False],
                [False, True , True , False],
                [False, True , True , False],
                [False, False, False, False],
            ],
            1, 1,
            3,
        ),
        (
            [
                [False, False, False],
                [True , True , True ],
                [False, False, False],
            ],
            0, -1,
            1,
        ),
        (
            [
                [False],
            ],
            0, 0,
            0,
        ),
        (
            [
                [False],
            ],
            1, 1,
            0,
        ),
    ))
    def test_living_neighbours(self, grid, row, col, expected):
        gen = Generation(grid)
        actual = gen.living_neighbours(row, col)
        assert actual == expected

    @pytest.mark.parametrize('gen1, gen2, expected', (
        (
            Generation([
                [False, True , False],
                [False, True , False],
                [False, True , False],
            ]),
            Generation([
                [False, True , False],
                [False, True , False],
                [False, True , False],
            ]),
            0,
        ),
        (
            Generation([
                [False, True , False],
                [False, True , False],
                [False, True , False],
            ]),
            Generation([
                [False, False, False],
                [True , True , True ],
                [False, False, False],
            ]),
            4,
        ),
    ))
    def test_xor(self, gen1, gen2, expected):
        actual = gen1 ^ gen2
        assert actual == expected

    @pytest.mark.parametrize('gen1, gen2, expected', (
        (
            Generation([
                [False, True , False],
                [False, True , False],
                [False, True , False],
            ]),
            Generation([
                [False, True , False],
                [False, True , False],
                [False, True , False],
            ]),
            True,
        ),
        (
            Generation([
                [False, True , False],
                [False, True , False],
                [False, True , False],
            ]),
            Generation([
                [False, False, False],
                [True , True , True ],
                [False, False, False],
            ]),
            False,
        ),
        (
            Generation([
                [False, True , False],
                [False, True , False],
                [False, True , False],
            ]),
            object(),
            False,
        ),
    ))
    def test_eq(self, gen1, gen2, expected):
        actual = gen1 == gen2
        assert actual == expected

    @pytest.mark.parametrize('grid, expected', (
        (
            [
                [False, True , False],
                [False, True , False],
                [False, True , False],
            ],
            ' 0 \n'
            ' 0 \n'
            ' 0 ',
        ),
        (
            [
                [False, False, False],
                [True , True , True ],
                [False, False, False],
            ],
            '   \n'
            '000\n'
            '   ',
        ),
        (
            [
                [False, False, False, False],
                [False, True , True , False],
                [False, True , True , False],
                [False, False, False, False],
            ],
            '    \n'
            ' 00 \n'
            ' 00 \n'
            '    ',
        ),
    ))
    def test_str(self, grid, expected):
        gen = Generation(grid)
        actual = str(gen)
        assert actual == expected
