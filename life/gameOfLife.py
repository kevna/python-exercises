#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys, random, os, time

class GameOfLife(object):
    GENERATIONSTOKEEP = 10
    
    def __init__(self, grid = []):
        self.grid = grid
        self.gridSize = 0
        for row in grid:
            self.gridSize += len(row)
        self.storedGenerations = []

    def compareGrids(self, gridA, gridB):
        matchCount = 0
        for row in range(len(gridA)):
            for col in range(len(gridA[row])):
                try:
                    if gridA[row][col] == gridB[row][col]:
                        matchCount += 1
                except IndexError:
                    pass
        return matchCount

    def hasActivity(self):
        generationCount = len(self.storedGenerations)
        if not generationCount:
            return True
        generationalMatch = 0
        for gridGeneration in self.storedGenerations:
            generationalMatch += self.compareGrids(gridGeneration, self.grid)
        generationalMatch /= generationCount
        return generationalMatch < self.gridSize * 0.99

    def storeGeneration(self):
        self.storedGenerations.append(self.grid)
        if len(self.storedGenerations) > self.GENERATIONSTOKEEP:
            del self.storedGenerations[0]

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
        self.storeGeneration()
        newGrid = []
        for row in range(len(self.grid)):
            newRow = []
            for col in range(len(self.grid[row])):
                newRow.append(self.cellLives(row, col))
            newGrid.append(tuple(newRow))
        self.grid = tuple(newGrid)
    
    def __str__(self):
        allRows = []
        for row in range(len(self.grid)):
            thisRow = []
            for col in range(len(self.grid[row])):
                if self.grid[row][col]:
                    thisRow.append("0") #"\xe2\x96\x88")
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
            newGrid.append(tuple(newRow))
        return tuple(newGrid)

    def theLoop(self):
        while self.hasActivity():
            self.step()
            os.system("clear")
            print self
            time.sleep(0.1)

    @staticmethod
    def main():
        rowMax = 20
        colMax = 40
        if len(sys.argv) == 3:
            rowMax = int(sys.argv[1])
            colMax = int(sys.argv[2])
        gameGrid = GameOfLife(GameOfLife.randomGrid(rowMax, colMax))
        try:
            gameGrid.theLoop()
        except KeyboardInterrupt:
            sys.exit(0)


if __name__ == "__main__":
    GameOfLife.main()
