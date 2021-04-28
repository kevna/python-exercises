#!/usr/bin/python2
# -*- coding: utf-8 -*-
from typing import Optional

from sudoku.ColourText import Colours, colour

class SudokuCell:
    """Cell model for a sudoku to solve."""
    ALLPOSSIBILITIES = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    ORIGINALCOLOUR = Colours.BLUE

    def __init__(self, value: Optional[int] = None):
        self.possibilities: list[int] = list(self.ALLPOSSIBILITIES)
        if value in self.ALLPOSSIBILITIES:
            self.value = value
            self.original = True
        else:
            self._value: Optional[int] = None
            self.original = False

    @property
    def value(self) -> Optional[int]:
        """Getter for value.
        This is trivial, but allows us to have a setter with validation.
        """
        return self._value

    @value.setter
    def value(self, value: int):
        """Setter for value.
        This blanks possibilites since the value is now set.
        :raises ValueError: when it's invalid to set the given value
        """
        if value not in self.possibilities:
            raise ValueError('Value {value} is not possible for cell')
        self._value = value
        self.possibilities = []

    def is_possible(self, possibility: int) -> bool:
        """Check if a value is still possible in this cell."""
        result = False
        if not self:
            result = possibility in self.possibilities
        elif possibility == self._value:
            result = True
        return result

    def remove_possibility(self, possibility: int) -> bool:
        """Remove a possibility from the cell.
        If there is only one possibility left then this is automatically set as value
        since this must be the case.
        """
        if self or not self.is_possible(possibility):
            return False
        self.possibilities.remove(possibility)
        if len(self.possibilities) <= 1:
            self.value = self.possibilities[0]
        return True

    def __bool__(self) -> bool:
        """Test if the cell's value has been found."""
        return self._value is not None

    def __len__(self) -> int:
        if self:
            result = 1
        else:
            result = len(self.possibilities)
        return result

    def __repr__(self) -> str:
        if self:
            result = f'{self._value}'
        else:
            result = f'{self.possibilities}'
        return result

    def __str__(self) -> str:
        result = ' '
        if self:
            result = f'{self._value}'
            if self.original:
                result = colour(result, self.ORIGINALCOLOUR)
        return result

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SudokuCell):
            return False
        result = False
        if self._value == other._value:
            result = True
            if not self:
                if set(self.possibilities) ^ set(other.possibilities):
                    return False
        return result
