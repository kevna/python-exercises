import sudokuSolver

class SudokuSolverSimple(sudokuSolver.SudokuSolver):
    def solveStep(self):
        cellsChanged = 0
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if self.grid[r][c].isFound():
                    n = self.grid[r][c].value
                    cellsChanged += self.grid.setValue(r, c, n)
        return cellsChanged


if __name__ == "__main__":
    SudokuSolverSimple.main()

