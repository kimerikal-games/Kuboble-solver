# Kuboble-solver

This is a solver for the [Kuboble puzzle](kuboble.com).

## Usage

The solver (`solver.py` or `solver.cpp`) takes a puzzle as input and outputs a solution if one exists.

The input is formatted as follows:

* The first line contains the number of `rows`, `columns` and `colors`.
* The next `rows` lines represent the puzzle grid. Each line contains `columns` characters, each representing a cell in the grid. A `.` represents an empty cell, and a `#` represents a blocked cell.
* The next `colors` lines represent the color information. Each line contains the color name, followed by the starting row and column, then the goal row and column.

For example, level 10 is represented as follows:

```
3 4 2
#.#.
....
#...
Green 2 3 1 1
Orange 2 2 0 3
```

## Performance

For the puzzles in kuboble.com, solution is obtained almost instantly.
The "very hard" puzzle below can be solved in about a minute (using PyPy or C++)

```
A B C D . . . .
. . . . . . . .
. . . . . . . .
. . a . . d . .
. . . . . . . .
b . . . . . . .
. . . . . . . c
. . . . . . . .
```
