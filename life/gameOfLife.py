#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys
import random

class GameOfLife(object):
    def __init__(self, grid = []):
        self.grid = grid
    
    def cellLives(self, x, y):
        liveNeigbours = 0
        height = len(self.grid)
        for i in range(-1, 2):
            posX = x + i
            if posX >= 0 and posX < height:
                width = len(self.grid[posX])
                for j in range(-1, 2):
                    posY = y + j
                    if posY >= 0 and posY < width and self.grid[posX][posY]:
                            liveNeigbours += 1
        liveCell = False
        if liveNeigbours == 3 or self.grid[x][y] and liveNeigbours == 4:
            liveCell = True
        return liveCell

    def step(self):
        newGrid = []
        for x in range(len(self.grid)):
            newRow = []
            for y in range(len(self.grid[x])):
                newRow.append(self.cellLives(x, y))
            newGrid.append(newRow)
        self.grid = newGrid
    
    def __str__(self):
        allRows = []
        for x in range(len(self.grid)):
            row = []
            for y in range(len(self.grid[x])):
                if self.grid[x][y]:
                    row.append("\xe2\x96\x88")
                else:
                    row.append(" ")
            allRows.append("".join(row))
        return "\n".join(allRows)

    @staticmethod
    def randomGrid(maxX, maxY):
        newGrid = []
        for x in range(maxX):
            newRow = []
            for y in range(maxY):
                if random.randint(0,3) == 1:
                    newRow.append(True)
                else:
                    newRow.append(False)
            newGrid.append(newRow)
        return newGrid

    @staticmethod
    def main():
        maxX = 10
        maxY = 10
        if len(sys.argv) == 3:
            maxX = int(sys.argv[1])
            maxY = int(sys.argv[2])
        gameGrid = GameOfLife(GameOfLife.randomGrid(maxX, maxY))
        try:
            while True:
                gameGrid.step()
                print gameGrid
        except KeyboardInterrupt:
            sys.exit(0)


if __name__ == "__main__":
    GameOfLife.main()
