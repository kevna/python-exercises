#!/usr/bin/python2
# -*- coding: utf-8 -*-
from unittest.mock import Mock

import pytest

from life.generation import Generation
from life.game_of_life import GameOfLife

class TestGameOfLife:
    tiny_false = Generation([[False]])
    tiny_true = Generation([[True]])

    @pytest.mark.parametrize('history, expected', (
        ([], True),
        ([tiny_false], True),
        ([tiny_true]*10, False),
        ([tiny_false]*10, True),
    ))
    def test_has_activity(self, history, expected):
        grid = GameOfLife(self.tiny_true)
        grid.history = history[:]
        actual = grid.has_activity()
        assert actual == expected

    @pytest.mark.parametrize('prehistory, generation, expected', (
        (
            [],
            tiny_false,
            [tiny_false],
        ),
        (
            [tiny_false]*10,
            tiny_true,
            [tiny_false]*9 + [tiny_true],
        ),
    ))
    def test_store_generation(self, prehistory, generation, expected):
        grid = GameOfLife(Generation([[]]))
        grid.history = prehistory[:]
        grid.store_generation(generation)
        assert grid.history == expected

    @pytest.mark.parametrize('alive, neighbours, expected', (
        (False, 2, False),
        (False, 3, True),
        (False, 4, False),
        (True, 1, False),
        (True, 2, True),
        (True, 3, True),
        (True, 4, False),
    ))
    def test_cell_lives(self, alive, neighbours, expected):
        mock_gen = Mock(spec=Generation)
        mock_gen._grid = [[]]
        mock_gen.alive.return_value = alive
        mock_gen.living_neighbours.return_value = neighbours
        grid = GameOfLife(mock_gen)
        actual = grid.cell_lives(0, 0)
        assert actual == expected

    @pytest.mark.parametrize('grid_arg, expected', (
        (
            (
                (False, True , False),
                (False, True , False),
                (False, True , False),
            ),
            (
                (False, False, False),
                (True , True , True ),
                (False, False, False),
            )
        ),
        (
            (
                (False, False, False, False),
                (False, True , True , False),
                (False, True , True , False),
                (False, False, False, False),
            ),
            (
                (False, False, False, False),
                (False, True , True , False),
                (False, True , True , False),
                (False, False, False, False),
            )
        ),
    ))
    def test_step(self, grid_arg, expected):
        grid = GameOfLife(Generation(grid_arg))
        actual = grid.step()
        assert actual == Generation(expected)
        assert actual == grid.current_gen
