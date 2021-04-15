#!/usr/bin/python2
# -*- coding: utf-8 -*-
import pytest

from sudoku.sudokuCell import SudokuCell

class TestSudokuCell:
    @pytest.mark.parametrize('testArgPoss, expectedResult', (
        (1, True),
        (0, False),
        (-1, False),
    ))
    def test_isPossible(self, testArgPoss, expectedResult):
        testCell = SudokuCell()
        actualResult = testCell.isPossible(testArgPoss)
        assert actualResult == expectedResult

    @pytest.mark.parametrize('testArgPossList, expectedPossibilities, expectedPossCount', (
        ([1], [2, 3, 4, 5, 6, 7, 8, 9], 8),
        ([1, 9], [2, 3, 4, 5, 6, 7, 8], 7),
        ([2, 3, 4, 5, 6, 7, 8, 9], None, 0),
        ([0], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9),
        ([-1], [1, 2, 3, 4, 5, 6, 7, 8, 9], 9),
    ))
    def test_removePosibility(self, testArgPossList, expectedPossibilities, expectedPossCount):
        testCell = SudokuCell()
        for testArgPoss in testArgPossList:
            testCell.removePossibility(testArgPoss)
        actualPossibilities = testCell.possibilities
        # TODO actualPossCount = testCell.possibilityCount
        assert actualPossibilities == expectedPossibilities
        # TODO assert actualPossCount == expectedPossCount

    @pytest.mark.parametrize('testArgValue, expectedResult', (
        (1, True),
        (0, False),
        (-1, False),
        (None, False),
    ))
    def test_isFound(self, testArgValue, expectedResult):
        testCell = SudokuCell(testArgValue)
        actualResult = testCell.isFound()
        assert actualResult == expectedResult

    @pytest.mark.parametrize('testArgValue, expectedResult', (
        (1, "1"),
        (0, "(1, 2, 3, 4, 5, 6, 7, 8, 9)"),
        (-1, "(1, 2, 3, 4, 5, 6, 7, 8, 9)"),
        (None, "(1, 2, 3, 4, 5, 6, 7, 8, 9)"),
    ))
    def test_str(self, testArgValue, expectedResult):
        testCell = SudokuCell(testArgValue)
        actualResult = str(testCell)
        assert actualResult == expectedResult

    @pytest.mark.parametrize('testArgValue1, testArgValue2, testArgPossList1, testArgPossList2, expectedResult', (
        (1, 1, [], [], True),
        (0, 0, [], [], True),
        (0, 0, [1, 2], [8, 9], False),
        (0, 0, [1, 9], [1, 9], True),
        (0, 1, [], [], False),
        (-1, 9, [], [], False),
        (None, 1, [], [], False),
        (0, -1, [], [], True),
    ))
    def test_eq(self, testArgValue1, testArgValue2, testArgPossList1, testArgPossList2, expectedResult):
        testCell1 = SudokuCell(testArgValue1)
        for testArgPoss in testArgPossList1:
            testCell1.removePossibility(testArgPoss)
        testCell2 = SudokuCell(testArgValue2)
        for testArgPoss in testArgPossList2:
            testCell2.removePossibility(testArgPoss)
        actualResult = testCell1 == testCell2
        assert actualResult == expectedResult
