#!/usr/bin/python2
# -*- coding: utf-8 -*-
from unittest.mock import Mock

import pytest

from life.generation import Generation
from life.game import Game
from life.rule import DEFAULT_RULE, Rule

@pytest.fixture
def rule():
    return Rule(DEFAULT_RULE)

class TestGame:
    tiny_false = Generation([[False]])
    tiny_true = Generation([[True]])

    @pytest.mark.parametrize('history, expected', (
        ([], True),
        ([tiny_false], True),
        ([tiny_true]*10, False),
        ([tiny_false]*10, True),
    ))
    def test_has_activity(self, history, expected, rule):
        grid = Game(self.tiny_true, rule)
        grid.history = history[:]
        actual = grid.has_activity()
        assert actual is expected

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
    def test_store_generation(self, prehistory, generation, expected, rule):
        grid = Game(self.tiny_true, rule)
        grid.history = prehistory[:]
        grid.store_generation(generation)
        assert grid.history == expected

    @pytest.mark.parametrize('rule, alive, neighbours, expected', (
        (DEFAULT_RULE, False, 2, False),
        (DEFAULT_RULE, False, 3, True),
        (DEFAULT_RULE, False, 4, False),
        (DEFAULT_RULE, True, 1, False),
        (DEFAULT_RULE, True, 2, True),
        (DEFAULT_RULE, True, 3, True),
        (DEFAULT_RULE, True, 4, False),
        ('B2', False, 2, True),
        ('B2', False, 3, False),
        ('B2', True, 2, False),
        ('B2', True, 3, False),
    ))
    def test_cell_lives(self, rule, alive, neighbours, expected):
        mock_gen = Mock(spec=Generation)
        mock_gen._grid = [[False]]
        mock_gen.alive.return_value = alive
        mock_gen.living_neighbours.return_value = neighbours
        grid = Game(mock_gen, Rule(rule))
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
    def test_step(self, grid_arg, expected, rule):
        grid = Game(Generation(grid_arg), rule)
        actual = grid.step()
        assert actual == Generation(expected)
        assert actual == grid.current_gen
        assert grid.generations == 1
