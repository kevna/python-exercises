#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sudokuCell

class SudokuGrid(object):
    GRID_HEIGHT = 9
    GRID_WIDTH = 9
    BOX_HEIGHT = 3
    BOX_WIDTH = 3
    def __init__(self, grid = []):
        newGrid = []
        for x in range(len(grid)):
            newRow = []
            for y in range(len(grid[x])):
                newRow.append(sudokuCell.SudokuCell(grid[x][y]))
            newGrid.append(newRow)
        self.grid = newGrid

    @classmethod
    def loadFile(self, fileName):
        newGrid = []
        with open(fileName) as fileHandle:
            for x in range(self.GRID_HEIGHT):
                newRow = []
                line = fileHandle.readline()
                for y in range(self.GRID_WIDTH):
                    try:
                        n = int(line[y])
                    except (ValueError, IndexError):
                        n = None
                    newRow.append(n)
                newGrid.append(newRow)
        return self(newGrid)

    def generateRow(self, width):
        row = []
        for y in range(width):
            if y % self.BOX_WIDTH == 0:
                row.append("|")
            row.append("-")
        row.append("|")
        return "-".join(row)

    def __str__(self):
        result = []
        width = 0
        for x in range(len(self.grid)):
            width = len(self.grid[x])
            if x % self.BOX_HEIGHT == 0:
                result.append(self.generateRow(width))
            row = []
            for y in range(width):
                if y % self.BOX_WIDTH == 0:
                    row.append("|")
                if self.grid[x][y].isFound():
                    row.append(str(self.grid[x][y]))
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
