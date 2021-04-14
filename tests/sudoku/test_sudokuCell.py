#!/usr/bin/python2
# -*- coding: utf-8 -*-
import unittest
from sudoku.sudokuCell import SudokuCell

class Test_SudokuCell(unittest.TestCase):
    def test_isPossible(self):
        testList = (
            (1, True),
            (0, False),
            (-1, False),
                )
        for testArgPoss, expectedResult in testList:
            testCell = SudokuCell()
            actualResult = testCell.isPossible(testArgPoss)
            self.assertEqual(expectedResult, actualResult)

    def test_removePosibility(self):
        testList = (
            ([1], [2, 3, 4, 5, 6, 7, 8, 9], 8),
            ([1, 9], [2, 3, 4, 5, 6, 7, 8], 7),
            ([2, 3, 4, 5, 6, 7, 8, 9], None, 0),
            ([0], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9),
            ([-1], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9),
                )
        for testArgPossList, expectedPossibilities, expectedPossCount in testList:
            testCell = SudokuCell()
            for testArgPoss in testArgPossList:
                testCell.removePossbility(testArgPoss)
            actualPossibilities = testCell.possibilities
            actualPossCount = testCell.possibilityCount
            self.assertEqual(expectedPossibilities, actualPossibilities)
            self.assertEqual(expectedPossCount, actualPossCount)

    def test_isFound(self):
        testList = (
            (1, True),
            (0, False),
            (-1, False),
            (None, False),
                )
        for testArgValue, expectedResult in testList:
            testCell = SudokuCell(testArgValue)
            actualResult = testCell.isFound()
            self.assertEqual(expectedResult, actualResult)

    def test_str(self):
        testList = (
            (1, "1"),
            (0, "(1, 2, 3, 4, 5, 6, 7, 8, 9)"),
            (-1, "(1, 2, 3, 4, 5, 6, 7, 8, 9)"),
            (None, "(1, 2, 3, 4, 5, 6, 7, 8, 9)"),
                )
        for testArgValue, expectedResult in testList:
            testCell = SudokuCell(testArgValue)
            actualResult = str(testCell)
            self.assertEqual(expectedResult, actualResult)

    def test_eq(self):
        testList = (
            (1, 1, [], [], True),
            (0, 0, [], [], True),
            (0, 0, [1, 2], [8, 9], False),
            (0, 0, [1, 9], [1, 9], True),
            (0, 1, [], [], False),
            (-1, 9, [], [], False),
            (None, 1, [], [], False),
            (0, -1, [], [], True),
                )
        for testArgValue1, testArgValue2, testArgPossList1, testArgPossList2, expectedResult in testList:
            testCell1 = SudokuCell(testArgValue1)
            for testArgPoss in testArgPossList1:
                testCell1.removePossbility(testArgPoss)
            testCell2 = SudokuCell(testArgValue2)
            for testArgPoss in testArgPossList2:
                testCell2.removePossbility(testArgPoss)
            actualResult = testCell1 == testCell2
            self.assertEqual(expectedResult, actualResult)


if  __name__ == "__main__":
    unittest.main()
