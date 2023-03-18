# Kuboble-solver

This is a solver for the [Kuboble puzzle](kuboble.com).

## Usage

The solver is implemented in `kuboble.py`. To use it, you need to set the following variables:
- `board`: a list of rows. If a piece can pass through a cell, mark it with a dot (`.`), otherwise use a hash symbol (`#`).
- `pieces`: a dictionary of piece names and their coordinates. Write the coordinates as `(row, column)` using 0-based indexing.
- `goals`: same as pieces, but for the destinations of the pieces.

## Performance

For simple puzzles, solution is obtained almost instantly.
For more harder puzzles, we recommend using [PyPy](https://www.pypy.org/) instead of CPython.
The "Hard" puzzle below can be solved in about 2 minutes (on my machine using PyPy).

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
