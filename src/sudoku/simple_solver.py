from sudoku.solver import SudokuSolver


class SudokuSolverSimple(SudokuSolver):
    """Solve sudokus using only beginer technique.
    """

    def row_remove_possibility(self, row: int, number: int) -> int:
        """Remove known value from the possibilities of the row."""
        result = 0
        for cell in self.grid[row]:
            if cell.remove_possibility(number):
                result += 1
        return result

    def col_remove_possibility(self, col: int, number: int) -> int:
        """Remove known value from the possibilities of the col."""
        result = 0
        for row in self.grid:
            if row[col].remove_possibility(number):
                result += 1
        return result

    def box_remove_possibility(self, cell_r: int, cell_c: int, number: int) -> int:
        """Remove known value from the possibilities in the box."""
        result = 0
        box_row, box_col = self.grid.get_box_coords(cell_r, cell_c)
        for row in range(box_row, box_row + self.grid.BOX_HEIGHT):
            for col in range(box_col, box_col + self.grid.BOX_WIDTH):
                if self.grid[row][col].remove_possibility(number):
                    result += 1
        return result

    def solve_step(self) -> int:
        """Perform a single step of solving the sudoku.
        This simply removes known values as possibilities from their row, col and box.
        """
        cells_changed = 0
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if number := self.grid[row][col].value:
                    cells_changed += self.row_remove_possibility(row, number)
                    cells_changed += self.col_remove_possibility(col, number)
                    cells_changed += self.box_remove_possibility(row, col, number)
        return cells_changed


if __name__ == '__main__':
    SudokuSolverSimple.main()
