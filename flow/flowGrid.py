#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys, flowCell

class FlowGrid(object):
    def __init__(self, grid = []):
        newGrid = []
        for row in grid:
            newRow = []
            for cell in row:
                newRow.append(flowCell.FlowCell(cell))
            newGrid.append(tuple(newRow))
        self._grid = tuple(newGrid)

    @classmethod
    def loadFile(self, fileName):
        newGrid = []
        with open(fileName) as fileHandle:
            line = fileHandle.readline()
            while line:
                newRow = []
                for c in line.strip("\r\n"):
                    newRow.append(c)
                newGrid.append(newRow)
                line = fileHandle.readline()
        return self(newGrid)

    def __len__(self):
        return len(self._grid)

    def __getitem__(self, key):
        return self._grid[key]

    def __str__(self):
        gridString = []
        for row in self._grid:
            rowString = []
            for cell in row:
                rowString.append(str(cell))
            gridString.append("".join(rowString))
        return "\n".join(gridString)


if __name__ == "__main__":
    grid = FlowGrid.loadFile(sys.argv[1])
    print grid
