#!/usr/bin/python2
# -*- coding: utf-8 -*-
from itertools import zip_longest
from typing import Sequence, Optional, Iterator

from ansi.colour import fg, fx  # type: ignore

from sudoku.cell import SudokuCell


UserGrid = Sequence[Sequence[Optional[int]]]
CellGrid = Sequence[Sequence[SudokuCell]]


class SudokuGrid:
    """Grid model for a suduko to solve."""
    GRID_HEIGHT = 9
    GRID_WIDTH = 9
    BOX_HEIGHT = 3
    BOX_WIDTH = 3

    COMPLETED_COLOUR = fg.green + fx.crossed_out

    LINECROS = '┼'
    LINEVERT = '│'
    LINEHORI = '─'

    def __init__(self, grid: UserGrid):
        self._complete_rows: list[int] = []
        self._complete_cols: list[int] = []
        self._complete_boxes: list[tuple[int, int]] = []
        new_grid = []
        for row in grid:
            new_row = []
            for cell in row:
                new_row.append(SudokuCell(cell))
            new_grid.append(tuple(new_row))
        self._grid: CellGrid = tuple(new_grid)

    @classmethod
    def load_file(cls, filename: str) -> 'SudokuGrid':
        """Factory to load a grid from a file."""
        new_grid = []
        with open(filename) as file:
            for _ in range(cls.GRID_HEIGHT):
                new_row = []
                line = file.readline()
                for col in range(cls.GRID_WIDTH):
                    try:
                        number: Optional[int] = int(line[col])
                    except (ValueError, IndexError):
                        number = None
                    new_row.append(number)
                new_grid.append(new_row)
        return cls(new_grid)

    def get_box_coords(self, cell_row: int, cell_col: int) -> tuple[int, int]:
        """Get the top-left cordinate of a sub-box within the sudoku grid.
        Top-left position makes it easy to iterate by the box's hight and width.
        """
        box_row = (cell_row // self.BOX_HEIGHT) * self.BOX_HEIGHT
        box_col = (cell_col // self.BOX_WIDTH) * self.BOX_WIDTH
        return box_row, box_col

    def row_complete(self, r: int) -> bool:
        """Check if an entire row has been completed."""
        if r in self._complete_rows:
            return True
        result = False
        for cell in self._grid[r]:
            if not cell:
                break
        else:
            self._complete_rows.append(r)
            result = True
        return result

    def col_complete(self, c: int) -> bool:
        """Check if an entire col has been completed."""
        if c in self._complete_cols:
            return True
        result = False
        for row in self._grid:
            if not row[c]:
                break
        else:
            self._complete_cols.append(c)
            result = True
        return result

    def box_complete(self, cell_row: int, cell_col: int) -> bool:
        """Check if an entire sub box has been completed."""
        box_row, box_col = self.get_box_coords(cell_row, cell_col)
        if (box_row, box_col) in self._complete_boxes:
            return True
        for row in range(box_row, box_row + self.BOX_HEIGHT):
            for col in range(box_col, box_col + self.BOX_WIDTH):
                if not self._grid[row][col]:
                    return False
        self._complete_boxes.append((box_row, box_col))
        return True

    def cell_complete(self, r: int, c: int) -> bool:
        """Check if a cell is in a completed row/box/cell."""
        return (
            self.row_complete(r)
            or self.col_complete(c)
            or self.box_complete(r, c)
        )

    def is_complete(self) -> bool:
        """Check if the entire grid has been completed."""
        for row in range(len(self._grid)):
            if not self.row_complete(row):
                return False
        return True

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, SudokuGrid):
            return False
        for our_row, their_row in zip_longest(self._grid, other._grid, fillvalue=[]):
            for our_cell, their_cell in zip_longest(our_row, their_row):
                if not our_cell == their_cell:
                    return False
        return True

    def row_separator(self, width: int) -> str:
        """This gets a row of separators between regions of the grid."""
        row = []
        for col in range(width):
            if col % self.BOX_WIDTH == 0:
                row.append(self.LINECROS)
            row.append(self.LINEHORI)
        row.append(self.LINECROS)
        return self.LINEHORI.join(row)

    def __str__(self) -> str:
        result = []
        found_count = 0
        possibility_count = 0
        hrule = self.row_separator(self.GRID_WIDTH)
        for r, row in enumerate(self._grid):
            if r % self.BOX_HEIGHT == 0:
                result.append(hrule)
            row_text = [self.LINEVERT]
            for c, cell in enumerate(row):
                if cell:
                    found_count += 1
                else:
                    possibility_count += len(cell)
                space = ' '
                cell_text = f'{cell}'
                if hl_whitespace := (self.row_complete(r) or self.box_complete(r, c)):
                    space = self.COMPLETED_COLOUR(space)
                if hl_whitespace or self.col_complete(c):
                    cell_text = self.COMPLETED_COLOUR(cell_text)
                row_text += [space, cell_text]
                if (c+1) % self.BOX_WIDTH == 0:
                    row_text += [space, self.LINEVERT]
            result.append(''.join(row_text))
        result += [
            hrule,
            f'Total Found: {found_count}',
            f'Remaining Possibilities: {possibility_count}',
        ]
        return '\n'.join(result)

    def __len__(self) -> int:
        return len(self._grid)

    def __getitem__(self, key: int) -> Sequence[SudokuCell]:
        return self._grid[key]

    def __iter__(self) -> Iterator[Sequence[SudokuCell]]:
        for row in self._grid:
            yield row


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
