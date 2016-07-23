import sudokuSolver

class SudokuSolverSimple(sudokuSolver.SudokuSolver):
    def rowRemovePossibility(self, r, n):
        result = 0
        for cell in self.grid[r]:
            if cell.removePossibility(n):
                result += 1
        return result

    def colRemovePossibility(self, c, n):
        result = 0
        for row in self.grid:
            if row[c].removePossibility(n):
                result += 1
        return result
    
    def boxRemovePossibility(self, r, c, n):
        result = 0
        R, C = self.grid.getBoxCoords(r, c)
        for row in range(R, R + self.grid.BOX_HEIGHT):
            for col in range(C, C + self.grid.BOX_WIDTH):
                if self.grid[row][col].removePossibility(n):
                    result += 1
        return result
    
    def solveStep(self):
        result = False
        cellsChanged = 0
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.grid[r][c].isFound():
                    n = self.grid[r][c].value
                    cellsChanged += self.rowRemovePossibility(r, n)
                    cellsChanged += self.colRemovePossibility(c, n)
                    cellsChanged += self.boxRemovePossibility(r, c, n)
        if cellsChanged > 0:
            result = cellsChanged
        return result


if __name__ == "__main__":
    SudokuSolverSimple.main()

