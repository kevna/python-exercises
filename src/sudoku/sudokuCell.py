#!/usr/bin/python2
# -*- coding: utf-8 -*-
from typing import Optional

from sudoku.ColourText import Colours, colour

class SudokuCell:
    """Cell model for a sudoku to solve."""
    ALLPOSSIBILITIES = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    ORIGINALCOLOUR = Colours.BLUE

    def __init__(self, value: Optional[int] = None):
        if value in self.ALLPOSSIBILITIES:
            self.set_value(value)
            self.original = True
        else:
            self.value: Optional[int] = None
            self.possibilities: list[int] = list(self.ALLPOSSIBILITIES)
            self.original = False

    def set_value(self, value: int):
        """Setter for value.
        This blanks possibilites since the value is now set.
        """
        self.value = value
        self.possibilities = []

    def is_possible(self, possibility: int) -> bool:
        """Check if a value is still possible in this cell."""
        result = False
        if not self.is_found():
            result = possibility in self.possibilities
        elif possibility == self.value:
            result = True
        return result

    def remove_possibility(self, possibility: int) -> bool:
        """Remove a possibility from the cell.
        If there is only one possibility left then this is automatically set as value
        since this must be the case.
        """
        if self.is_found() or not self.is_possible(possibility):
            return False
        self.possibilities.remove(possibility)
        if len(self.possibilities) <= 1:
            self.set_value(self.possibilities[0])
        return True

    def is_found(self) -> bool:
        """Test if the cell's value has been found."""
        return self.value is not None

    def __len__(self) -> int:
        if self.is_found():
            result = 1
        else:
            result = len(self.possibilities)
        return result

    def __repr__(self) -> str:
        if self.is_found():
            result = f'{self.value}'
        else:
            result = f'{self.possibilities}'
        return result

    def __str__(self) -> str:
        result = ' '
        if self.is_found():
            result = f'{self.value}'
            if self.original:
                result = colour(result, self.ORIGINALCOLOUR)
        return result

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SudokuCell):
            return False
        result = False
        if self.value == other.value:
            result = True
            if not self.is_found():
                for i in self.possibilities:
                    if i not in other.possibilities:
                        return False
                for j in other.possibilities:
                    if j not in self.possibilities:
                        return False
        return result
