#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys, random, time

class GameOfLife(object):
    def __init__(self, grid = []):
        self.grid = grid
    
    def cellLives(self, row, col):
        liveNeigbours = 0
        height = len(self.grid)
        for i in range(-1, 2):
            rowPos = row + i
            if rowPos >= 0 and rowPos < height:
                width = len(self.grid[rowPos])
                for j in range(-1, 2):
                    colPos = col + j
                    if colPos >= 0 and colPos < width and self.grid[rowPos][colPos]:
                            liveNeigbours += 1
        liveCell = False
        if liveNeigbours == 3 or self.grid[row][col] and liveNeigbours == 4:
            liveCell = True
        return liveCell

    def step(self):
        newGrid = []
        for row in range(len(self.grid)):
            newRow = []
            for col in range(len(self.grid[row])):
                newRow.append(self.cellLives(row, col))
            newGrid.append(newRow)
        self.grid = newGrid
    
    def __str__(self):
        allRows = []
        for row in range(len(self.grid)):
            thisRow = []
            for col in range(len(self.grid[row])):
                if self.grid[row][col]:
                    thisRow.append("\xe2\x96\x88")
                else:
                    thisRow.append(" ")
            allRows.append("".join(thisRow))
        return "\n".join(allRows)

    @staticmethod
    def randomGrid(rowMax, colMax):
        newGrid = []
        for row in range(rowMax):
            newRow = []
            for col in range(colMax):
                if random.randint(0,3) == 1:
                    newRow.append(True)
                else:
                    newRow.append(False)
            newGrid.append(newRow)
        return newGrid

    @staticmethod
    def main():
        rowMax = 20
        colMax = 30
        if len(sys.argv) == 3:
            rowMax = int(sys.argv[1])
            colMax = int(sys.argv[2])
        gameGrid = GameOfLife(GameOfLife.randomGrid(rowMax, colMax))
        try:
            while True:
                gameGrid.step()
                print gameGrid
                time.sleep(0.1)
        except KeyboardInterrupt:
            sys.exit(0)


if __name__ == "__main__":
    GameOfLife.main()
