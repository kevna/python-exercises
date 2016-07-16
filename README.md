Python Exercises
================
A collection of programming exercises written in python for practice and to pass the time.

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