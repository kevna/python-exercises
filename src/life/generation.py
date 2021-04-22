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

    def living_neighbours(self, row: int, col: int) -> int:
        """Test whether a cell should survive from the previous generation into a new one.
        This is done by counting the 8 (orthogonal and diagonal) neighbouring cells
        and then applying the classic game of life rules: B3/S23.
        """
        live_neighbours = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                row_pos = row + i
                col_pos = col + j
                if row_pos >= 0 and col_pos >= 0 and self.alive(row_pos, col_pos):
                    live_neighbours += 1
        if self.alive(row, col):
            live_neighbours -= 1
        return live_neighbours

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
        for row in self._grid:
            line = []
            for cell in row:
                if cell:
                    line.append('0') #'\xe2\x96\x88')
                else:
                    line.append(' ')
            result.append(''.join(line))
        return '\n'.join(result)
