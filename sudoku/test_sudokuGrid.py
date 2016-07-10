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
