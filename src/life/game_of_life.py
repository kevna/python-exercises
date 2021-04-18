#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys
from random import randint
import os
import time
from typing import Sequence

from itertools import zip_longest

GameGrid = Sequence[Sequence[bool]]

class GameOfLife:
    """Simulation of Jogn Conways game of life."""
    GENERATIONSTOKEEP = 10

    def __init__(self, grid: GameGrid):
        self.grid = grid
        self.grid_size = 0
        for row in grid:
            self.grid_size += len(row)
        self.stored_generations: list[GameGrid] = []

    def compare_grids(self, grid_a: GameGrid, grid_b: GameGrid):
        """Compare generations of the internal grid representation.
        This counts the cells that are in matching state between the grids.
        """
        matches = 0
        for row_a, row_b in zip_longest(grid_a, grid_b, fillvalue=[]):
            for cell_a, cell_b in zip_longest(row_a, row_b):
                if cell_a == cell_b:
                    matches += 1
        return matches

    def has_activity(self):
        """Hueristically estimate if the life cycle of the game grid
        has reached a stable state.
        We can only estimate since finite oscillators can be constructed of (almost) any period.
        eg. p46-based PRNG survives 40894 generations, more than we want to store.

        The hueristic takes a simple average of matching cells across stored generations
        this is compared to a static confidence threshold (currently  99%)
        """
        generations = len(self.stored_generations)
        if not generations:
            return True
        generational_average = 0
        for generation in self.stored_generations:
            generational_average += self.compare_grids(generation, self.grid)
        generational_average /= generations
        return generational_average < self.grid_size * 0.99

    def store_generation(self):
        """Add the current grid generation to the generation store.
        This also maintains the length of the generation store to conserve memory.
        """
        self.stored_generations.append(self.grid)
        if len(self.stored_generations) > self.GENERATIONSTOKEEP:
            del self.stored_generations[0]

    def cell_lives(self, row: int, col: int) -> bool:
        """Test whether a cell should survive from the previous generation into a new one.
        This is done by counting the 8 (orthogonal and diagonal) neighbouring cells
        and then applying the classic game of life rules: B3/S23.
        """
        live_neigbours = 0
        height = len(self.grid)
        for i in range(-1, 2):
            row_pos = row + i
            if 0 <= row_pos < height:
                width = len(self.grid[row_pos])
                for j in range(-1, 2):
                    col_pos = col + j
                    if 0 <= col_pos < width and self.grid[row_pos][col_pos]:
                        live_neigbours += 1
        live_cell = False
        if live_neigbours == 3 or self.grid[row][col] and live_neigbours == 4:
            live_cell = True
        return live_cell

    def step(self):
        """Pprogress a single generation in the game of life.
        This generates a new generation since if the previous were modified
        new cells would affect the life-counts of the neighbours tested after.
        """
        self.store_generation()
        new_grid = []
        for row in range(len(self.grid)):
            new_row = []
            for col in range(len(self.grid[row])):
                new_row.append(self.cell_lives(row, col))
            new_grid.append(tuple(new_row))
        self.grid = tuple(new_grid)

    def __str__(self):
        """Render the current generations as a contiguous text block."""
        result = []
        for row in self.grid:
            line = []
            for cell in row:
                if cell:
                    line.append('0') #'\xe2\x96\x88')
                else:
                    line.append(' ')
            result.append(''.join(line))
        return '\n'.join(result)

    @staticmethod
    def random_grid(rows: int, cols: int) -> GameGrid:
        """Generate a new randomly-distributed grid."""
        new_grid = []
        for _ in range(rows):
            new_row = []
            for _ in range(cols):
                if randint(0,3) == 1:
                    new_row.append(True)
                else:
                    new_row.append(False)
            new_grid.append(tuple(new_row))
        return tuple(new_grid)

    def the_loop(self):
        """Perform the game by iterating steps until activity ceases.
        At each generation we clear the screen and display the current generation.
        We sleep for 0.1 seconds between each generations.
        """
        while self.has_activity():
            self.step()
            os.system('clear')
            print(self)
            time.sleep(0.1)

    @staticmethod
    def main():
        """Main method to allow basic terminal interaction
        by specifying the grid size and handling ^C.
        """
        rows = 20
        cols = 40
        if len(sys.argv) == 3:
            rows = int(sys.argv[1])
            cols = int(sys.argv[2])
        game_grid = GameOfLife(GameOfLife.random_grid(rows, cols))
        try:
            game_grid.the_loop()
        except KeyboardInterrupt:
            sys.exit(0)


if __name__ == '__main__':
    GameOfLife.main()
