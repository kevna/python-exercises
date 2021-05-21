#!/usr/bin/python2
# -*- coding: utf-8 -*-
from math import log

from life.generation import Generation
from life.rule import Rule


class Game:
    """Simulation of John Conways game of life."""
    GENERATIONSTOKEEP = 10

    def __init__(self, gen: Generation, rule: Rule):
        self.current_gen = gen
        self.height = len(gen._grid)
        self.width = len(gen._grid[0])
        area = self.height*self.width
        self.end_threshold = area/(50*log(area))
        self.history: list[Generation] = []
        self.generations = 0
        self.rule = rule

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
            if differences := self.current_gen ^ generation:
                generational_average += differences
            else:
                # If generations are identical the only life left is
                # still life or ocillators with period <= GENERATIONSTOKEEP
                return False
        generational_average /= len(self.history)
        return generational_average > self.end_threshold

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
        surviving = self.current_gen.alive(row, col)
        live_neighbours = self.current_gen.living_neighbours(row, col)
        if (surviving and live_neighbours in self.rule.survival) \
                or (not surviving and live_neighbours in self.rule.birth):
            return True
        return False

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
        self.generations += 1
        return self.current_gen

    def __iter__(self):
        """Iterate the game to proceed through generations."""
        while self.has_activity():
            yield self.step()
