#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sudokuCell

class SolveFailedException(Exception):
    pass

class SudokuGrid(object):
    GRID_HEIGHT = 9
    GRID_WIDTH = 9
    BOX_HEIGHT = 3
    BOX_WIDTH = 3
    def __init__(self, grid = []):
        newGrid = []
        for r in range(len(grid)):
            newRow = []
            for c in range(len(grid[r])):
                newRow.append(sudokuCell.SudokuCell(grid[r][c]))
            newGrid.append(newRow)
        self.grid = newGrid

    @classmethod
    def loadFile(self, fileName):
        newGrid = []
        with open(fileName) as fileHandle:
            for r in range(self.GRID_HEIGHT):
                newRow = []
                line = fileHandle.readline()
                for c in range(self.GRID_WIDTH):
                    try:
                        n = int(line[c])
                    except (ValueError, IndexError):
                        n = None
                    newRow.append(n)
                newGrid.append(newRow)
        return self(newGrid)

    def rowRemovePossibility(r, n):
        for c in range(len(self.grid[r])):
            self.grid[r][c].removePossibility(n)

    def colRemovePossibility(c, n):
        for r in range(len(self.grid)):
            self.grid[r][c].removePossibility(n)

    def isComplete(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if not self.grid[r][c].isFound():
                    return False
        return True

    def __eq__(self, other):
        if not isinstance(other, SudokuGrid):
            return False
        result = True
        try:
            for r in range(len(self.grid)):
                for c in range(len(self.grid[r])):
                    if not self.grid[r][c] == other.grid[r][c]:
                        return False
        except IndexError:
            # An index on self.grid didn't exist in other.grid so they must be different shapes
            result = False
        return result

    def generateRow(self, width):
        row = []
        for c in range(width):
            if c % self.BOX_WIDTH == 0:
                row.append("|")
            row.append("-")
        row.append("|")
        return "-".join(row)

    def __str__(self):
        result = []
        width = 0
        for r in range(len(self.grid)):
            width = len(self.grid[r])
            if r % self.BOX_HEIGHT == 0:
                result.append(self.generateRow(width))
            row = []
            for c in range(width):
                if c % self.BOX_WIDTH == 0:
                    row.append("|")
                if self.grid[r][c].isFound():
                    row.append(str(self.grid[r][c]))
                else:
                    row.append(" ")
            row.append("|")
            result.append(" ".join(row))
        result.append(self.generateRow(width))
        return"\n" .join(result)


if __name__ == "__main__":
    fileName = "testData/web.sud"
    grid = SudokuGrid.loadFile(fileName)
    print grid
