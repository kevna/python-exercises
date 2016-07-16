Python Exercises
================
A collection of programming exercises written in python for practice and to pass the time.

ackermann
---------
Ackermann's function is one of the earliest examples of a totally computable (μ-recursive) function that is not also a primitive recursive function. It is doubly-recursive and grows more quickly than even many multiple exponential functions. To read more about Ackermann's function [visit wolfram mathworld](http://mathworld.wolfram.com/AckermannFunction.html)

current features:
- calculate ackermann's function up to the maximum under the recursion limit of the device used
- cache values of completed calculations to reduce recursion in additional calls
- store and load "cache file" with pre-calculated cache data
- graceful fail raises overflow error without stack-trace of the entire reccursion
  + error is only raised by the top-level function call
- multiple "main" processes:
  + "grid" approach iterates n within m up to a given limit
  + "find result" approach seeks out the values of m and n that can return a given result

future additions:
- additional arguments
  + choice of "main" process
    * "grid" and "find result" approaches
    * individual ackermann result
  + choice to use/not use cache file
    * option to give name for cache file

life
----
John Conway's game of life is a "zero player game", a simple simulator for cellular automata.
To find out more about the game of life [visit the life wiki](http://www.conwaylife.com/wiki/Main_Page), a fantastic resource for a variety of patterns.

current features:
- Arguments can be used to specify grid size
- Random population of the grid
- Heuristic analysis estimates the cessation of activity within the grid

future additions:
- load "pattern files" to provide editable start-states
- additional life forms within the simulation
  + int or byte could replace bool as the cell model to enable this
  + should consider interaction between different life forms (which ones kill off which others)
- alternative handling for edges of the simulation grid
  + "normal" handling simulates a border of permenantly dead cells beyond the grid edge
  + how would the simulation change if edges were permenantly alive?
  + a popular alternative is a torus-wrapped world with top flowing onto bottom and left onto right
- additional arguments:
  + timing between generational steps
  + command arguments for above additions