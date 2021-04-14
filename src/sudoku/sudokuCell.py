#!/usr/bin/python2
# -*- coding: utf-8 -*-
from sudoku import ColourText

class SudokuCell(object):
    ALLPOSSIBILITIES = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    ORIGINALCOLOUR = ColourText.BLUE
    
    def __init__(self, value = None):
        if value in self.ALLPOSSIBILITIES:
            self.setValue(value)
            self.original = True
        else:
            self.value = None
            self.possibilities = list(self.ALLPOSSIBILITIES)
            self.original = False

    def setValue(self, value):
        self.value = value
        self.possibilities = None

    def isPossible(self, possibility):
        result = False
        if not self.isFound():
            result = possibility in self.possibilities
        elif possibility == self.value:
            result = True
        return result

    def removePossibility(self, possibility):
        if self.isFound() or not self.isPossible(possibility):
            return False
        self.possibilities.remove(possibility)
        if len(self.possibilities) <= 1:
            self.setValue(self.possibilities[0])
        return True

    def isFound(self):
        return self.value is not None

    def __len__(self):
        if self.isFound():
            result = 1
        else:
            result = len(self.possibilities)
        return result

    def __repr__(self):
        if self.isFound():
            result = self.value
        else:
            result = self.possibilities
        return str(result)

    def __str__(self):
        result = " "
        if self.isFound():
            result = str(self.value)
            if self.original:
                result = ColourText.colour(result, self.ORIGINALCOLOUR)
        return result

    def __eq__(self, other):
        if not isinstance(other, SudokuCell):
            return False
        result = False
        if self.value == other.value:
            result = True
            if not self.isFound():
                for i in self.possibilities:
                    if i not in other.possibilities:
                        return False
                for j in other.possibilities:
                    if i not in self.possibilities:
                        return False
        return result
