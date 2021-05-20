#!/usr/bin/python2
# -*- coding: utf-8 -*-
from random import randint
from typing import Sequence
from itertools import zip_longest


Grid = Sequence[Sequence[bool]]


class Generation:
    """Model for a single generation of John Conways game of life."""

    def __init__(self, grid: Grid):
        self._grid = grid
        self.neighbours = self.generate_neighbours()

    @classmethod
    def random(cls, height: int, width: int) -> 'Generation':
        """Generate a new randomly-distributed grid."""
        new_grid = []
        for _ in range(height):
            new_row = []
            for _ in range(width):
                new_row.append(randint(0,3) == 1)
            new_grid.append(new_row)
        return cls(new_grid)

    def alive(self, row: int, col: int) -> bool:
        """Test whether a cell is alive."""
        try:
            return self._grid[row][col]
        except IndexError:
            return False

    def generate_neighbours(self) -> Sequence[Sequence[int]]:
        neighbours = [[0]*len(row) for row in self._grid]
        for Y, row in enumerate(self._grid):
            for X, cell in enumerate(row):
                if cell:
                    for y in range(-1, 2):
                        for x in range(-1, 2):
                            row_pos = Y + y
                            col_pos = X + x
                            if row_pos >= 0 and col_pos >= 0 and not (x == 0 and y == 0):
                                try:
                                    neighbours[row_pos][col_pos] += 1
                                except IndexError:
                                    pass
        return neighbours

    def living_neighbours(self, row: int, col: int) -> int:
        """Test whether a cell should survive from the previous generation into a new one.
        This is done by counting the 8 (orthogonal and diagonal) neighbouring cells
        and then applying the classic game of life rules: B3/S23.
        """
        return self.neighbours[row][col]

    def __xor__(self, other: 'Generation') -> int:
        """Compare generations of the internal grid representation.
        This counts the cells that are in matching state between the grids.
        """
        differences = 0
        for our_row, their_row in zip_longest(self._grid, other._grid, fillvalue=[]):
            for our_cell, their_cell in zip_longest(our_row, their_row):
                if our_cell != their_cell:
                    differences += 1
        return differences

    def __eq__(self, other: object) -> bool:
        """Test exact equality between generation grids.
        The loops are identical to xor but we can skip out at the first difference.
        This offers far better average performance for large grids (worst case is the same).
        """
        if not isinstance(other, Generation):
            return False
        for our_row, their_row in zip_longest(self._grid, other._grid, fillvalue=[]):
            for our_cell, their_cell in zip_longest(our_row, their_row):
                if our_cell != their_cell:
                    return False
        return True

    def __str__(self):
        """Render the current generations as a contiguous text block."""
        result = []
        for upper, lower in zip_longest(self._grid[::2], self._grid[1::2], fillvalue=[]):
            line = []
            for upper_cell, lower_cell in zip_longest(upper, lower, fillvalue=False):
                if upper_cell and lower_cell:
                    line.append('█')
                elif upper_cell:
                    line.append('▀')
                elif lower_cell:
                    line.append('▄')
                else:
                    line.append(' ')
            result.append(''.join(line))
        return '\n'.join(result)
