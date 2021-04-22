#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys
import os
import time

from life.generation import Generation


class GameOfLife:
    """Simulation of John Conways game of life."""
    GENERATIONSTOKEEP = 10

    def __init__(self, gen: Generation):
        self.current_gen = gen
        self.height = len(gen._grid)
        self.width = len(gen._grid[0])
        self.history: list[Generation] = []

    def has_activity(self):
        """Hueristically estimate if the life cycle of the game grid
        has reached a stable state.
        We can only estimate since finite oscillators can be constructed of (almost) any period.
        eg. p46-based PRNG survives 40894 generations, more than we want to store.

        The hueristic takes a simple average of matching cells across stored generations
        this is compared to a static confidence threshold (currently  99%)
        """
        if not self.history:
            return True
        generational_average = 0
        for generation in self.history:
            generational_average += self.current_gen ^ generation
        generational_average /= len(self.history)
        return generational_average > (0.01*self.height*self.width)

    def store_generation(self, generation):
        """Add the current grid generation to the generation store.
        This also maintains the length of the generation store to conserve memory.
        """
        self.history.append(generation)
        if len(self.history) > self.GENERATIONSTOKEEP:
            del self.history[0]

    def cell_lives(self, row: int, col: int) -> bool:
        """Test whether a cell should survive from the previous generation into a new one.
        This is done by counting the 8 (orthogonal and diagonal) neighbouring cells
        and then applying the classic game of life rules: B3/S23.
        """
        live_neighbours = self.current_gen.living_neighbours(row, col)
        live_cell = False
        if live_neighbours == 3 or (self.current_gen.alive(row, col) and live_neighbours == 2):
            live_cell = True
        return live_cell

    def step(self):
        """Progress a single generation in the game of life.
        This generates a new generation since if the previous were modified
        new cells would affect the life-counts of the neighbours tested after.
        """
        self.store_generation(self.current_gen)
        new_grid = []
        for row in range(self.height):
            new_row = []
            for col in range(self.width):
                new_row.append(self.cell_lives(row, col))
            new_grid.append(new_row)
        self.current_gen = Generation(new_grid)
        return self.current_gen

    def __iter__(self):
        """Iterate the game to proceed through generations."""
        while self.has_activity():
            yield self.step()

    def the_loop(self):
        """Perform the game by iterating steps until activity ceases.
        At each generation we clear the screen and display the current generation.
        We sleep for 0.1 seconds between each generations.
        """
        for generation in self:
            os.system('clear')
            print(generation)
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
        game_grid = GameOfLife(Generation.random(rows, cols))
        try:
            game_grid.the_loop()
        except KeyboardInterrupt:
            sys.exit(0)


if __name__ == '__main__':
    GameOfLife.main()
