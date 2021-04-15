#!/usr/bin/python2
# -*- coding: utf-8 -*-
import pytest

from sudoku.sudokuGrid import SudokuGrid

class TestSudokuGrid:
    @pytest.mark.parametrize('testArgPoss, expectedResult', (
        (1, True),
        (0, False),
        (-1, False),
    ))
    def _test_isPossible(self, testArgPoss, expectedResult):
        testCell = sudokuCell.SudokuCell()
        actualResult = testCell.isPossible(testArgPoss)
        assert actualResult == expectedResult

    @pytest.mark.parametrize('testArgGrid, testArgR, testArgN, expectedPossibilities', (
        #([], True),
        #([[]], True),
        #([
        #    [1, 2, 3, 4, 5, 6, 7, 8, 9],
        #], True),
        #([
        #    [1, 2, 3, 4, None, 6, 7, 8, 9],
        #], False),
        #(-1, None),
    ))
    def test_rowRemovePossibility(self, testArgGrid, testArgR, testArgN, expectedPossibilities):
        testGrid = SudokuGrid(testArgGrid)
        testGrid.rowRemovePossibility(testArgR, testArgN)
        for expectedKey in expectedPossibilities:
            expectedResult = expectedPossibilities[expectedKey]
            actualResult = testGrid.grid[0][expectedKey]
            assert actualResult == expectedResult

    @pytest.mark.parametrize('testArgGrid, expectedResult', (
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
    ))
    def test_isComplete(self, testArgGrid, expectedResult):
        testGrid = SudokuGrid(testArgGrid)
        actualResult = testGrid.isComplete()
        assert actualResult == expectedResult

    @pytest.mark.parametrize('testArgGrid1, testArgGrid2, expectedResult', (
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
    ))
    def test_eq(self, testArgGrid1, testArgGrid2, expectedResult):
        testGrid1 = SudokuGrid(testArgGrid1)
        testGrid2 = SudokuGrid(testArgGrid2)
        actualResult = testGrid1 == testGrid2
        assert actualResult == expectedResult

    @pytest.mark.parametrize('testArgGrid, expectedResult', (
        ([], "|"),
        ([[]], "|\n|\n|"),
        ([
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
        ], "|-------|-------|-------|\n| 1 2 3 | 4 5 6 | 7 8 9 |\n| 2 3 4 | 5 6 7 | 8 9 1 |\n|-------|-------|-------|"),
        #(-1, None),
    ))
    def test_str(self, testArgGrid, expectedResult):
        testGrid = SudokuGrid(testArgGrid)
        actualResult = str(testGrid)
        assert actualResult == expectedResult
