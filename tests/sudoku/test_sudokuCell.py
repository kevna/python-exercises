#!/usr/bin/python2
# -*- coding: utf-8 -*-
import pytest

from sudoku.sudokuCell import SudokuCell


class TestSudokuCell:
    @pytest.mark.parametrize('possibility, expected', (
        (1, True),
        (0, False),
        (-1, False),
    ))
    def test_is_possible(self, possibility, expected):
        cell = SudokuCell()
        actual = cell.is_possible(possibility)
        assert actual == expected

    @pytest.mark.parametrize('possibilities, expected_possibilities', (
        ([1], [2, 3, 4, 5, 6, 7, 8, 9]),
        ([1, 9], [2, 3, 4, 5, 6, 7, 8]),
        ([2, 3, 4, 5, 6, 7, 8, 9], []),
        ([0], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([-1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ))
    def test_remove_posibility(self, possibilities, expected_possibilities):
        cell = SudokuCell()
        for possibility in possibilities:
            cell.remove_possibility(possibility)
        actual_possibilities = cell.possibilities
        assert actual_possibilities == expected_possibilities

    @pytest.mark.parametrize('value, expected', (
        (1, True),
        (0, False),
        (-1, False),
        (None, False),
    ))
    def test_is_found(self, value, expected):
        cell = SudokuCell(value)
        actual = cell.is_found()
        assert actual == expected

    @pytest.mark.parametrize('value, expected', (
        (1, '1'),
        (0, '[1, 2, 3, 4, 5, 6, 7, 8, 9]'),
        (-1, '[1, 2, 3, 4, 5, 6, 7, 8, 9]'),
        (None, '[1, 2, 3, 4, 5, 6, 7, 8, 9]'),
    ))
    def test_repr(self, value, expected):
        cell = SudokuCell(value)
        actual = repr(cell)
        assert actual == expected

    @pytest.mark.parametrize('value, expected', (
        (1, '\x1b[94m1\x1b[0m'),
        (0, ' '),
        (None, ' '),
    ))
    def test_str_original(self, value, expected):
        cell = SudokuCell(value)
        actual = str(cell)
        assert actual == expected

    @pytest.mark.parametrize('value, expected', (
        (1, '1'),
        (None, ' '),
    ))
    def test_str_found(self, value, expected):
        cell = SudokuCell()
        cell.set_value(value)
        actual = str(cell)
        assert actual == expected

    @pytest.mark.parametrize('value1, value2, possibilities1, possibilities2, expected', (
        (1, 1, [], [], True),
        (0, 0, [], [], True),
        (0, 0, [1, 2], [8, 9], False),
        (0, 0, [1, 9], [1, 9], True),
        (0, 1, [], [], False),
        (-1, 9, [], [], False),
        (None, 1, [], [], False),
        (0, -1, [], [], True),
    ))
    def test_eq(self, value1, value2, possibilities1, possibilities2, expected):
        cell1 = SudokuCell(value1)
        for possibility in possibilities1:
            cell1.remove_possibility(possibility)
        cell2 = SudokuCell(value2)
        for possibility in possibilities2:
            cell2.remove_possibility(possibility)
        actual = cell1 == cell2
        assert actual == expected
