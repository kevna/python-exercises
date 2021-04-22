ackermann
---------
- [ ] make the caching more generic by moving from a 2D dict `cache[m][n]=a` to an args tuple `cache[(m,n)]=a`
- [ ] consider if caching can be done as a decorator rather than integrating it into the function
- [ ] consider if we should move `cache.__str__` to `cache.__repr__` since it's not intended for public consumption

life
----
- [X] consider separating the grid properties and game logic into two classes
    - this would make it easier to enforce grids being immutable
    - compare_grids could be replaced with Grid.__xor__ by counting differences rather than matches
    - perhaps Game.__iter__ handles the step function by yielding the new game grid?
- [ ] move parseargs and the cli app loop to `__main__`
- [ ] accept rule strings

sorting
-------
- [ ] sorter parent class should be abstract, sort should be abstract method
- [ ] potentially more pythonic to return the sorted list rather than mutating the original
    - since this can be done with a slice it may also impact the time comparison less
- [ ] create hybrid implementations of qick and merge sorts
    - hybrid algorithms switch to a more efficient algorithm for short lists
    - [ ] use cutoff to switch alg and prevent stack overflow
- [ ] consider looking at parallelising recursive sorts
- [ ] consider pivot-picking for quick sort

sudoku
------
- [ ] make cell value a property
    - set_value then becomes an assignment
    - we should probably be freezing the value once assigned
- [ ] make `cell.is_found` into `cell.__bool__`
- [ ] use set symmetric_difference in `cell.__eq__`
- [ ] check_ can be removed from methods when they're type-hinted as returning boolean
- [ ] SudokuSolver should be abstract, solve_step should be abstractmethod
- [ ] consider giving cell object awareness of it's coordinate
    - if we do this we can iterate the cells and get the row/col without using enumerate
    - we could also then maintain a list of found cells, this could offer a vast speed bost to the simple solver
        - perhaps newly known, as these are the ones likely to change the next results
- [ ] add validation method to the sudoku grid
