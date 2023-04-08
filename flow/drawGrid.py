#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys, flowGrid, curses

class DrawGrid(object):
    LINECROS = "┼"
    LINEVERT = "│"
    LINEHORI = "─"

    def __init__(self, grid):
        self._grid = grid
        self.window = curses.initscr()
        

    def generateRow(self, width):
        row = [self.LINECROS]
        row += [self.LINEHORI]*width
        row.append(self.LINECROS)
        return self.LINEHORI.join(row)

    def drawBorders(self):
        self.window.addstr(0, 1, "-" * len(self._grid[0]))
        for r in range(len(self._grid)):
            self.window.addstr(r + 1, 0, "|")
            self.window.addstr(r + 1, len(self._grid[r]) + 1, "|")
        self.window.addstr(r+2, 1, "-" * len(self._grid[r]))

    def drawCell(self, row, col):
        self.window.addstr(row+1, col+1, str(self._grid[row][col]))

    def drawGrid(self):
        self.window.clear()
        self.drawBorders()
        for r in range(len(self._grid)):
            for c in range(len(self._grid[r])):
                self.drawCell(r, c)
        self.window.refresh()


if __name__ == "__main__":
    grid = DrawGrid(flowGrid.FlowGrid.loadFile(sys.argv[1]))
    try:
        grid.drawGrid()
        grid.window.getch()
    finally:
        curses.endwin()
