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
- [X] move parseargs and the cli app loop to `__main__`
- [X] accept rule strings
- [ ] implement RLE file format
    - This will allow us to save and restore the state of a game
    - We will also be able to use examples from the life wiki
    - https://conwaylife.com/wiki/Run_Length_Encoded
- [ ] refactor to make more use of standard life language
    - eg. generation.random -> soup/broth
        - consider adding density property to this (and as arg)
- [ ] work on speeding up processing between generations
    - can we calculate the neighbourhoods progressively (or otherwise in bulk) rather than recomputing the overlap multiple times?
- [ ] consider performing analysis on the end result to decide some of the following:
    - if the universe has become stable we could identify strict/pseudo/quasi still lives
    - if the heuristic has ended it we should be able to identify short-period oscillators
- [ ] consider if we can recognise small patterns and highlight them on the fly
    - this would look cool and could be very informative
    - it could be too resource intensive, especially for large grids or lots of debris
- [ ] consider how we can add support for wrapping grids
    - this should be able to be implemented within the living_neighbours implementation
    - should this be an option on the current generation or a new implementation?
- [ ] consider how we could add support for different neighbourhood geometries
    - this should be able to be implemented within the living_neighbours implementation
    - these should definitely be implemented as different generation objects
- [ ] consider how we can add support for different cell shapes (eg. triangular/hexagonal)
    - these should definitely be implemented as different generation objects
    - solving the different neighbourhoods from above should greatly simplify this
    - we may need to look at implementing a graphical display to properly display them
    - there may be additional changes needed to the workflow loop

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
- [X] make cell value a property
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
