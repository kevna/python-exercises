#!/usr/bin/python2
# -*- coding: utf-8 -*-
from ansi.colour import fx  # type: ignore
import pytest

from sudoku.cell import SudokuCell


class TestSudokuCell:
    @pytest.mark.parametrize('value', (1, 9))
    def test_set_value(self, value):
        cell = SudokuCell()
        cell.value = value
        assert cell.value == value
        assert cell.possibilities == []

    @pytest.mark.parametrize('value', (0, 10, None))
    def test_set_value_validation(self, value):
        cell = SudokuCell()
        with pytest.raises(ValueError):
            cell.value = value

    def test_set_value_reset(self):
        cell = SudokuCell(4)
        with pytest.raises(ValueError):
            cell.value = 2

    @pytest.mark.parametrize('value, possibility, expected', (
        (5, 5, True),
        (5, 1, False),
        (None, 1, True),
        (None, 0, False),
        (None, -1, False),
    ))
    def test_is_possible(self, value, possibility, expected):
        cell = SudokuCell(value)
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
    def test_bool(self, value, expected):
        cell = SudokuCell(value)
        actual = bool(cell)
        assert actual == expected


    @pytest.mark.parametrize('value, possibilities, actual', (
        (None, [1, 2, 3, 4, 5, 6, 7, 8, 9], 9),
        (None, [2, 3, 4, 6, 7, 8], 6),
        (9, [], 1),
    ))
    def test_len(self, value, possibilities, actual):
        cell = SudokuCell(value)
        cell.possibilities = possibilities
        assert len(cell) == actual

    @pytest.mark.parametrize('value, expected', (
        (1, '1'),
        (9, '9'),
        (0, '[1, 2, 3, 4, 5, 6, 7, 8, 9]'),
        (-1, '[1, 2, 3, 4, 5, 6, 7, 8, 9]'),
        (None, '[1, 2, 3, 4, 5, 6, 7, 8, 9]'),
    ))
    def test_repr(self, value, expected):
        cell = SudokuCell(value)
        actual = repr(cell)
        assert actual == expected

    @pytest.mark.parametrize('value, expected', (
        (1, fx.bold('1')),
        (9, fx.bold('9')),
        (0, ' '),
        (None, ' '),
    ))
    def test_str_original(self, value, expected):
        cell = SudokuCell(value)
        actual = str(cell)
        assert actual == expected

    @pytest.mark.parametrize('value, expected', (
        (1, fx.italic('1')),
        (9, fx.italic('9')),
        (None, ' '),
    ))
    def test_str_found(self, value, expected):
        cell = SudokuCell()
        try:
            cell.value = value
        except ValueError:
            pass
        actual = str(cell)
        assert actual == expected

    @pytest.mark.parametrize('value1, value2, possibilities1, possibilities2, expected', (
        (1, 1, [], [], True),
        (0, 0, [], [], True),
        (None, None, [1, 2], [8, 9], False),
        (None, None, [8, 9], [7, 8, 9], False),
        (None, None, [1, 9], [1, 9], True),
        (0, 1, [], [], False),
        (-1, 9, [], [], False),
        (None, 1, [], [], False),
        (0, -1, [], [], True),
    ))
    def test_eq(self, value1, value2, possibilities1, possibilities2, expected):
        cell1 = SudokuCell(value1)
        cell1.possibilities = possibilities1
        cell2 = SudokuCell(value2)
        cell2.possibilities = possibilities2
        actual = cell1 == cell2
        assert actual == expected

    def test_eq_type(self):
        cell = SudokuCell(1)
        actual = cell == 1
        assert actual is False
