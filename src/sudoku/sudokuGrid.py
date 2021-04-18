#!/usr/bin/python2
# -*- coding: utf-8 -*-
from itertools import zip_longest

from sudoku.sudokuCell import SudokuCell
from sudoku import ColourText


class SudokuGrid:
    """Grid model for a suduko to solve."""
    GRID_HEIGHT = 9
    GRID_WIDTH = 9
    BOX_HEIGHT = 3
    BOX_WIDTH = 3

    COMPLETEDCOLOURCELL = ColourText.GREEN
    COMPLETEDCOLOURLINE = ColourText.PINK

    LINECROS = '┼'
    LINEVERT = '│'
    LINEHORI = '─'

    def __init__(self, grid):
        self._complete_rows = []
        self._complete_cols = []
        self._complete_boxes = []
        new_grid = []
        for row in grid:
            new_row = []
            for cell in row:
                new_row.append(SudokuCell(cell))
            new_grid.append(tuple(new_row))
        self._grid = tuple(new_grid)

    @classmethod
    def load_file(cls, filename):
        """Factory to load a grid from a file."""
        new_grid = []
        with open(filename) as file:
            for _ in range(cls.GRID_HEIGHT):
                new_row = []
                line = file.readline()
                for col in range(cls.GRID_WIDTH):
                    try:
                        number = int(line[col])
                    except (ValueError, IndexError):
                        number = None
                    new_row.append(number)
                new_grid.append(new_row)
        return cls(new_grid)

    def get_box_coords(self, cell_row, cell_col):
        """Get the top-left cordinate of a sub-box within the sudoku grid.
        Top-left position makes it easy to iterate by the box's hight and width.
        """
        box_row = (cell_row // self.BOX_HEIGHT) * self.BOX_HEIGHT
        box_col = (cell_col // self.BOX_WIDTH) * self.BOX_WIDTH
        return box_row, box_col

    def check_row_complete(self, r):
        """Check if an entire row has been completed."""
        if r in self._complete_rows:
            return True
        result = False
        for cell in self._grid[r]:
            if not cell.is_found():
                break
        else:
            self._complete_rows.append(r)
            result = True
        return result

    def check_col_complete(self, c):
        """Check if an entire col has been completed."""
        if c in self._complete_cols:
            return True
        result = False
        for row in self._grid:
            if not row[c].is_found():
                break
        else:
            self._complete_cols.append(c)
            result = True
        return result

    def check_box_complete(self, cell_row, cell_col):
        """Check if an entire sub box has been completed."""
        box_row, box_col = self.get_box_coords(cell_row, cell_col)
        if (box_row, box_col) in self._complete_boxes:
            return True
        for row in range(box_row, box_row + self.BOX_HEIGHT):
            for col in range(box_col, box_col + self.BOX_WIDTH):
                if not self._grid[row][col].is_found():
                    return False
        self._complete_boxes.append((box_row, box_col))
        return True

    def check_cell_complete(self, r, c):
        """Check if a cell is in a completed row/box/cell."""
        return (
            self.check_row_complete(r)
            or self.check_col_complete(c)
            or self.check_box_complete(r, c)
        )

    def is_complete(self):
        """Check if the entire grid has been completed."""
        for row in range(len(self._grid)):
            if not self.check_row_complete(row):
                return False
        return True

    def __eq__(self, other):
        if not isinstance(other, SudokuGrid):
            return False
        for our_row, their_row in zip_longest(self._grid, other._grid, fillvalue=[]):
            for our_cell, their_cell in zip_longest(our_row, their_row):
                if not our_cell == their_cell:
                    return False
        return True

    def row_separator(self, width):
        """This gets a row of separators between regions of the grid."""
        row = []
        for col in range(width):
            if col % self.BOX_WIDTH == 0:
                row.append(self.LINECROS)
            line = self.LINEHORI
            if self.check_col_complete(col):
                line = ColourText.colour(line, self.COMPLETEDCOLOURLINE)
            row.append(line)
        row.append(self.LINECROS)
        return self.LINEHORI.join(row)

    def __str__(self):
        result = []
        found_count = 0
        possibility_count = 0
        width = 0
        for r, row in enumerate(self._grid):
            width = len(row)
            if r % self.BOX_HEIGHT == 0:
                result.append(self.row_separator(width))
            line = self.LINEVERT
            if self.check_row_complete(r):
                line = ColourText.colour(line, self.COMPLETEDCOLOURLINE)
            row_text = []
            for c, cell in enumerate(row):
                if c % self.BOX_WIDTH == 0:
                    row_text.append(line)
                cell_text = str(cell)
                if cell.is_found():
                    found_count += 1
                else:
                    possibility_count += len(cell)
                if self.check_cell_complete(r, c):
                    cell_text = ColourText.colour(cell_text, self.COMPLETEDCOLOURCELL)
                row_text.append(cell_text)
            row_text.append(line)
            result.append(' '.join(row_text))
        result.append(self.row_separator(width))
        result.append(f'Total Found: {found_count}')
        result.append(f'Remaining Possibilities: {possibility_count}')
        return'\n' .join(result)

    def __len__(self):
        return len(self._grid)

    def __getitem__(self, key):
        return self._grid[key]

    @staticmethod
    def main():
        """Load basic sudoku file and display it.
        This allows for manual testing during rapid-prototyping.
        """
        filename = 'testData/web.sud'
        grid = SudokuGrid.load_file(filename)
        print(grid)


if __name__ == '__main__':
    SudokuGrid.main()
