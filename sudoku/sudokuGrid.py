#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sudokuCell, ColourText

class SudokuGrid(object):
    GRID_HEIGHT = 9
    GRID_WIDTH = 9
    BOX_HEIGHT = 3
    BOX_WIDTH = 3

    COMPLETEDCOLOURCELL = ColourText.GREEN
    COMPLETEDCOLOURLINE = ColourText.PINK

    LINECROS = "┼"
    LINEVERT = "│"
    LINEHORI = "─"

    def __init__(self, grid = []):
        self._completeRows = []
        self._completeCols = []
        self._completeBoxes = []
        newGrid = []
        for r in range(len(grid)):
            newRow = []
            for c in range(len(grid[r])):
                newRow.append(sudokuCell.SudokuCell(grid[r][c]))
            newGrid.append(tuple(newRow))
        self._grid = tuple(newGrid)
        self.failedSteps = 0

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

    def getBoxCoords(self, r, c):
        subgridR = (r / self.BOX_HEIGHT) * self.BOX_HEIGHT
        subgridC = (c / self.BOX_WIDTH) * self.BOX_WIDTH
        return subgridR, subgridC

    def checkRowComplete(self, r):
        if r in self._completeRows:
            return True
        result = False
        for c in range(len(self._grid[r])):
            if not self._grid[r][c].isFound():
                break
        else:
            self._completeRows.append(r)
            result = True
        return result

    def checkColComplete(self, c):
        if c in self._completeCols:
            return True
        result = False
        for r in range(len(self._grid)):
            if not self._grid[r][c].isFound():
                break
        else:
            self._completeCols.append(c)
            result = True
        return result

    def checkBoxComplete(self, r, c):
        R, C = self.getBoxCoords(r, c)
        if (R, C) in self._completeBoxes:
            return True
        for row in range(R, R + self.BOX_HEIGHT):
            for col in range(C, C + self.BOX_WIDTH):
                if not self._grid[row][col].isFound():
                    return False
        self._completeBoxes.append((R, C))
        return True

    def checkCellComplete(self, r, c):
        return self.checkRowComplete(r) or self.checkColComplete(c) or self.checkBoxComplete(r, c)

    def isComplete(self):
        for r in range(len(self._grid)):
            if not self.checkRowComplete(r):
                return False
        return True


    def __eq__(self, other):
        if not isinstance(other, SudokuGrid):
            return False
        result = True
        try:
            for r in range(len(self._grid)):
                for c in range(len(self._grid[r])):
                    if not self._grid[r][c] == other.grid[r][c]:
                        return False
        except IndexError:
            # An index on self._grid didn't exist in other.grid so they must be different shapes
            result = False
        return result

    def generateRow(self, width):
        row = []
        for c in range(width):
            if c % self.BOX_WIDTH == 0:
                row.append(self.LINECROS)
            line = self.LINEHORI
            if self.checkColComplete(c):
                line = ColourText.colour(line, self.COMPLETEDCOLOURLINE)
            row.append(line)
        row.append(self.LINECROS)
        return self.LINEHORI.join(row)

    def __str__(self):
        result = []
        foundCount = 0
        possibilityCount = 0
        width = 0
        for r in range(len(self._grid)):
            width = len(self._grid[r])
            if r % self.BOX_HEIGHT == 0:
                result.append(self.generateRow(width))
            line = self.LINEVERT
            if self.checkRowComplete(r):
                line = ColourText.colour(line, self.COMPLETEDCOLOURLINE)
            row = []
            for c in range(width):
                if c % self.BOX_WIDTH == 0:
                    row.append(line)
                cellText = str(self._grid[r][c])
                if self._grid[r][c].isFound():
                    foundCount += 1
                else:
                    possibilityCount += len(self._grid[r][c])
                if self.checkCellComplete(r, c):
                    cellText = ColourText.colour(cellText, self.COMPLETEDCOLOURCELL)
                row.append(cellText)
            row.append(line)
            result.append(" ".join(row))
        result.append(self.generateRow(width))
        result.append("Total Found: %d" % foundCount)
        result.append("Remaining Possibilities: %d" % possibilityCount)
        return"\n" .join(result)
    
    def __len__(self):
        return len(self._grid)

    def __getitem__(self, key):
        return self._grid[key]
    
    @staticmethod
    def main():
        fileName = "testData/web.sud"
        grid = SudokuGrid.loadFile(fileName)
        print grid

if __name__ == "__main__":
    SudokuGrid.main()
