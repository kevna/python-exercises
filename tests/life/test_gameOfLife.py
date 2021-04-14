#!/usr/bin/python2
# -*- coding: utf-8 -*-
import unittest
from life.gameOfLife import GameOfLife

class Test_GameOfLife(unittest.TestCase):
    def test_cellLives(self):
        testList = (
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
                )
        for startGrid, testArgX, testArgY, expectedResult in testList:
            testGrid = GameOfLife(startGrid)
            actualResult = testGrid.cellLives(testArgX, testArgY)
            self.assertEqual(expectedResult, actualResult)
    
    def test_step(self):
        testList = (
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
                )
        for startGrid, expectedResult in testList:
            testGrid = GameOfLife(startGrid)
            testGrid.step()
            actualResult = testGrid.grid
            self.assertEqual(expectedResult, actualResult)

    def test_str(self):
        testList = (
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
                )
        for startGrid, expectedResult in testList:
            testGrid = GameOfLife(startGrid)
            actualResult = str(testGrid)
            self.assertEqual(expectedResult, actualResult)

    def test_randomGrid(self):
        testList = (
            (0, 0, 0, 0),
            (1, 0, 1, 0),
            (10, 10, 10, 10),
            (50, 100, 50, 100),
            (-1, -10, 0, 0),
            #([], 0, 0, False),
                )
        for testArgX, testArgY, expectedX, expectedY in testList:
            testGrid = GameOfLife.randomGrid(testArgX, testArgY)
            actualX = len(testGrid)
            self.assertEqual(expectedX, actualX)
            for x in testGrid:
                actualY = len(x)
                self.assertEqual(expectedY, actualY)


if __name__ == "__main__":
    unittest.main()
