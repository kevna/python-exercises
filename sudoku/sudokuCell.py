#!/usr/bin/python2
# -*- coding: utf-8 -*-

class SudokuCell(object):
    ALLPOSSIBILITIES = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    
    def __init__(self, value = None):
        if value in self.ALLPOSSIBILITIES:
            self.value = value
            self.possibilityCount = 0
            self.possibilities = None
        else:
            self.value = None
            self.possibilityCount = 9
            self.possibilities = list(self.ALLPOSSIBILITIES)

    def isPossible(self, possibility):
        result = possibility in self.possibilities
        if self.isFound() and possibility == self.value:
            result = True
        return result

    def removePossbility(self, possibility):
        if possibility == self.value or not self.isPossible(possibility):
            return False
        self.possibilities.remove(possibility)
        self.possibilityCount -= 1
        if self.possibilityCount == 1:
            value = self.possibilities[0]
            self.possibilities = None
            self.possibilityCount = 0
        return True

    def isFound(self):
        return self.value is not None

    def __str__(self):
        if self.isFound():
            result = str(self.value)
        else:
            possList = []
            for i in self.possibilities:
                possList.append(str(i))
            result = "(" + ", ".join(possList) + ")"
        return result

    def __eq__(self, other):
        if not isinstance(other, SudokuCell):
            return False
        result = False
        if self.value == other.value:
            if self.isFound():
                result = True
            else:
                result = True
                for i in self.possibilities:
                    if i not in other.possibilities:
                        result = False
                for j in other.possibilities:
                    if i not in self.possibilities:
                        result = False
        return result
