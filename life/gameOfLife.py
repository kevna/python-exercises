#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys, random, os, time, curses, argparse

class GameOfLife(object):
    GENERATIONSTOKEEP = 10
    
    def __init__(self, grid = [], sleep = 0.1):
        self.grid = grid
        self.sleep = sleep
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

        liveCell = (liveNeigbours-1) in {True: (2, 3), # survival case
                                         False: (2,), # birth case
                                         }[self.grid[row][col]]
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

    def drawGrid(self):
        os.system("clear")
        print self

    def drawCursesGrid(self):
        #self.window.clear()
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                cellChar = " "
                if self.grid[row][col]:
                    cellChar = "0" #"\xe2\x96\x88"
                self.window.addch(row, col, cellChar)
        self.window.refresh()

    def drawCursesMessage(self, message):
        self.window.addstr(len(self.grid) + 1, 0, message)
        self.window.refresh()

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
        self.window = curses.initscr()
        curses.noecho()
        try:
            while self.hasActivity():
                self.step()
                self.drawCursesGrid()
                time.sleep(self.sleep)
            self.drawCursesMessage("Game Over, press any key to exit")
            self.window.getch()
        finally:
            curses.endwin()

    @staticmethod
    def fetchArgs():
        parser = argparse.ArgumentParser(description = "Play the Game of Life")
        parser.add_argument("-r", "--rows", type = int, default = 20, help = "Height of the game grid")
        parser.add_argument("-c", "--cols", type = int, default = 40, help = "Width of the game grid")
        parser.add_argument("-s", "--sleep", type = float, default = 0.1, help = "Time between game steps")
        return parser.parse_args()

    @staticmethod
    def main():
        args = GameOfLife.fetchArgs()
        gameGrid = GameOfLife(grid = GameOfLife.randomGrid(args.rows, args.cols), sleep = args.sleep)
        try:
            gameGrid.theLoop()
        except KeyboardInterrupt:
            sys.exit(0)


if __name__ == "__main__":
    GameOfLife.main()
