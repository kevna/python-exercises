#!/usr/bin/python2
# -*- coding: utf-8 -*-
import Script
import re
import CursesMixin
import sys, random, os, time, curses

class GameOfLife(Script.Script, CursesMixin.CursesMixin):
    GENERATIONSTOKEEP = 10
    RULESETS = {"life": ({2, 3}, {2,}),
                "highlife": ({2, 3}, {3, 6}),
                "seeds": ({}, {2,}),
                "maze": ({1, 2, 3, 4, 5}, {3,}),
                "flock": ({1, 2}, {3,}),
                }
    
    def __init__(self, grid = []):
        self.rows = 20
        self.cols = 40
        self.rules = {True: (2, 3), # survival case
                      False: (2,), # birth case
                      }
        self.setGrid(grid)
        self.storedGenerations = []
        self.cellColour = 0

    def fetchArgParser(self):
        parser = super(GameOfLife, self).fetchArgParser(description = "Play the game of life")
        parser.add_argument("-s", "--size", type = str, default = "%sx%s"%(self.rows,self.cols), help = "dimensions of the game grid")
        parser.add_argument("-r", "--rules", type = str, default = "life", help = "Rule set to use for this game")
        parser.add_argument("--sleep", type = float, default = 0.1, help = "Time between game steps")
        parser.add_argument("--die", action="store_true", help = "Die when game appears to be over")
        parser.add_argument("--colour", action="store_true", help = "Colour the game grid")
        return parser

    def validateConfig(self):
        super(GameOfLife, self).validateConfig()
        match = re.match("(\d+)x(\d+)", self.config.size)
        if match:
            self.rows, self.cols = [int(d) for d in match.groups()]

        rules = self.config.rules
        survival = ()
        birth = ()
        if self.config.rules in self.RULESETS:
            survival, birth = self.RULESETS[rules]
        else:
            match = re.match("(\d*)/(\d*)", rules)
            if match:
                survival, birth = match.groups()
            else:
                match = re.match("B(\d*)/S(\d*)", rules)
                if match:
                    birth, survival = match.groups()
        if survival or birth:
            self.rules = {True: {int(d) for d in survival},
                          False: {int(d) for d in birth},
                          }

    def _main(self):
        grid = self.randomGrid(self.rows, self.cols)
        self.setGrid(grid)
        self.cursesStart(colour = self.config.colour)
        try:
            self.theLoop()
        finally:
            self.cursesEnd()

    def cursesStart(self, colour = False):
        super(GameOfLife, self).cursesStart(colour = colour)
        if colour:
            self.cellColour = curses.color_pair(11)

    def setGrid(self, grid):
        self.grid = grid
        self.gridSize = 0
        for row in grid:
            self.gridSize += len(row)
        
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

        liveCell = (liveNeigbours-1) in self.rules[self.grid[row][col]]
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
                    cellChar = curses.ACS_DIAMOND
                self.window.addch(row, col, cellChar, self.cellColour)
        self.window.refresh()

    def drawCursesMessage(self, message):
        super(GameOfLife, self).drawCursesMessage(len(self.grid) + 1, 0, message)

    def randomGrid(self, rowMax, colMax):
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
        repeat = True
        while repeat:
            self.step()
            self.drawCursesGrid()
            time.sleep(self.config.sleep)
            if self.config.die:
                repeat = self.hasActivity()
        self.drawCursesMessage("Game Over, press any key to exit")
        self.window.getch()


if __name__ == "__main__":
    game = GameOfLife()
    game.main()
