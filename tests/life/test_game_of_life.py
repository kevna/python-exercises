#!/usr/bin/python2
# -*- coding: utf-8 -*-
import pytest

from life.game_of_life import GameOfLife

class TestGameOfLife:
    @pytest.mark.parametrize('startGrid, testArgX, testArgY, expectedResult', (
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
    def test_cell_lives(self, startGrid, testArgX, testArgY, expectedResult):
        testGrid = GameOfLife(startGrid)
        actualResult = testGrid.cell_lives(testArgX, testArgY)
        assert actualResult == expectedResult
    
    @pytest.mark.parametrize('startGrid, expectedResult', (
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
    def test_step(self, startGrid, expectedResult):
        testGrid = GameOfLife(startGrid)
        testGrid.step()
        actualResult = testGrid.grid
        assert actualResult == expectedResult

    @pytest.mark.parametrize('startGrid, expectedResult', (
        ([
            [False, True , False],
            [False, True , False],
            [False, True , False],
        ], " \xe2\x96\x88 \n \xe2\x96\x88 \n \xe2\x96\x88 "),
        ([
            [False, False, False],
            [True , True , True ],
            [False, False, False],
        ], "   \n\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n   "),
        ([
            [False, False, False, False],
            [False, True , True , False],
            [False, True , True , False],
            [False, False, False, False],
        ], "    \n \xe2\x96\x88\xe2\x96\x88 \n \xe2\x96\x88\xe2\x96\x88 \n    "),
        #([], 0, 0, False),
    ))
    def test_str(self, startGrid, expectedResult):
        testGrid = GameOfLife(startGrid)
        actualResult = str(testGrid)
        assert actualResult == expectedResult

    @pytest.mark.parametrize('testArgX, testArgY, expectedX, expectedY', (
        (0, 0, 0, 0),
        (1, 0, 1, 0),
        (10, 10, 10, 10),
        (50, 100, 50, 100),
        (-1, -10, 0, 0),
        #([], 0, 0, False),
    ))
    def test_random_grid(self, testArgX, testArgY, expectedX, expectedY):
        testGrid = GameOfLife.random_grid(testArgX, testArgY)
        actualX = len(testGrid)
        assert actualX == expectedX
        for x in testGrid:
            actualY = len(x)
            assert actualY == expectedY
