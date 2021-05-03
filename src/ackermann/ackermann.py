#!/usr/bin/python2
# -*- coding: utf-8 -*-
import sys

class AckermannOverflowError(RuntimeError):
    """Error class for ackermann"""

class AckermannCache:
    """Calculate Ackermann values.
    We've also built a simple cache using a dict and able to be persisted with a file.
    """
    CACHEFILE = 'cacheFile.dat'

    def __init__(self):
        sys.setrecursionlimit(25000)
        self.cache: dict[tuple, int] = {}
        self.size = 0
        self.read_size = 0

    def add_cache(self, args: tuple, value: int):
        """Add a result to the internal cache."""
        self.cache[args] = value
        self.size += 1

    def get_cache(self, args: tuple) -> int:
        """Get a result from the internal cache."""
        try:
            result = self.cache[args]
        except KeyError:
            result = False
        return result

    def load_cache(self, filename: str):
        """Load a cache record from a persistant file."""
        with open(filename) as file:
            for line in file:
                m, n, value = line.strip().split(',')
                self.add_cache((int(m), int(n)), int(value))
        self.read_size = self.size

    def save_cache(self, filename: str):
        """Save a cache record to a persistant file."""
        if self.size <= self.read_size:
            return
        with open(filename, 'w') as file:
            for (m, n), value in self.cache.items():
                print(f'{m},{n},{value}', file=file)

    def get_ackermann(self, m: int, n: int) -> int:
        """Calculate the ackermann-péter function of m and n.
        This is recursive and grows quite quickly.
        Caching is used to avoid re-computing known values.
        """
        result = self.get_cache((m, n))
        if result:
            return result
        result = 0
        try:
            if m < 1:
                result = n + 1
            elif n < 1:
                result = self.get_ackermann(m-1, 1)
            else:
                result = self.get_ackermann(m-1, self.get_ackermann(m, n-1))
            self.add_cache((m, n), result)
        except RuntimeError as error:
            raise AckermannOverflowError(
                f'Recursion limit of {sys.getrecursionlimit()}'
                f'reached calculating Ackermann({m}, {n})'
            ) from error
        return result

    def __str__(self):
        """Show the contents of the cache for debugging purposes."""
        result = []
        for (m, n), value in self.cache.items():
            result.append(f'({m}, {n}) = {value}')
        return '\n'.join(result)

    def ackermann_grid(self):
        """Experiment with pre-populating the cache.
        This method builds the cache up from the lowest values of m and n.
        Doing so can reduce the computational complexity of generating the next generation
        similar to the function of ackermann_to.
        """
        max_m = 6
        max_n = 6
        arguments = len(sys.argv)
        if arguments > 2:
            max_m = int(sys.argv[1])
            max_n = int(sys.argv[2])
        elif arguments == 2:
            max_n = int(sys.argv[1])
        for m in range(max_m):
            for n in range(max_n):
                ackermann = self.get_ackermann(m, n)
                print(f'Ackermann({m}, {n}) is {ackermann}')

    def ackermann_to(self):
        """Calculate ackermann values from 0,0 to a given maximum.
        This builds up the cache values which reduces the needed recursion depth.
        """
        max_ackermann = 65533
        arguments = len(sys.argv)
        if arguments > 1:
            max_ackermann = int(sys.argv[1])
        m = 0
        ackermann = 0
        while ackermann < max_ackermann or m < max_ackermann:
            m += 1
            n = 0
            ackermann = 0
            while ackermann < max_ackermann:
                n += 1
                ackermann = self.get_ackermann(m, n)
            print(f'Ackermann({m}, {n}) is {ackermann}')

    @staticmethod
    def main():
        """Wrapper function to load and save the persistant cache file.
        Also provides some handling of anticipated errors to avoid tracebacks.
        """
        cache = AckermannCache()
        cache.load_cache(AckermannCache.CACHEFILE)
        try:
            cache.ackermann_to()
        except AckermannOverflowError:
            print(cache.size)
        except KeyboardInterrupt:
            sys.exit(0)
        cache.save_cache(AckermannCache.CACHEFILE)


if __name__ == '__main__':
    AckermannCache.main()
