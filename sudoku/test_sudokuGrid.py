#!/usr/bin/python2
# -*- coding: utf-8 -*-
import unittest
import sudokuGrid

class Test_SudokuGrid(unittest.TestCase):
    def _test_isPossible(self):
        testList = (
            (1, True),
            (0, False),
            (-1, False),
                )
        for testArgPoss, expectedResult in testList:
            testCell = sudokuCell.SudokuCell()
            actualResult = testCell.isPossible(testArgPoss)
            self.assertEqual(expectedResult, actualResult)

    def test_rowRemovePossibility(self):
        testList = (
            ([], True),
            ([[]], True),
            ([
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
            ], True),
            ([
                [1, 2, 3, 4, None, 6, 7, 8, 9],
            ], False),
            #(-1, None),
                )
        for testArgGrid, testArgR, testArgN, expectedPossibilities in testList:
            testGrid = sudokuGrid.SudokuGrid(testArgGrid)
            testGrid.rowRemovePossibility(testArgR, testArgN)
            for expectedKey in expectedPossibilities:
                expectedResult = expectedPossibilities[expectedKey]
                actualResult = testGrid.grid[0][expectedKey]
                self.assertEqual(expectedResult, actualResult)

    def test_isComplete(self):
        testList = (
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
                )
        for testArgGrid, expectedResult in testList:
            testGrid = sudokuGrid.SudokuGrid(testArgGrid)
            actualResult = testGrid.isComplete()
            self.assertEqual(expectedResult, actualResult)

    def test_eq(self):
        testList = (
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
                )
        for testArgGrid1, testArgGrid2, expectedResult in testList:
            testGrid1 = sudokuGrid.SudokuGrid(testArgGrid1)
            testGrid2 = sudokuGrid.SudokuGrid(testArgGrid2)
            actualResult = testGrid1 == testGrid2
            self.assertEqual(expectedResult, actualResult)

    def test_str(self):
        testList = (
            ([], "|"),
            ([[]], "|\n|\n|"),
            ([
                [1, 2, 3, 4, 5, 6, 7, 8, 9],
                [2, 3, 4, 5, 6, 7, 8, 9, 1],
            ], "|-------|-------|-------|\n| 1 2 3 | 4 5 6 | 7 8 9 |\n| 2 3 4 | 5 6 7 | 8 9 1 |\n|-------|-------|-------|"),
            #(-1, None),
                )
        for testArgGrid, expectedResult in testList:
            testGrid = sudokuGrid.SudokuGrid(testArgGrid)
            actualResult = str(testGrid)
            self.assertEqual(expectedResult, actualResult)


if  __name__ == "__main__":
    unittest.main()
