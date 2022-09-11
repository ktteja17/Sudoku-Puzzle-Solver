# Sudoku Solver

This is a Python program that solves Sudoku puzzles.

## Files and Folders

The important files and folders are described here:

``` text
.
├── puzzles                 # folder containing example suduko grids, and their solutions
├── solve.py                # the main entry point for this app
├── solver                  # module that contains all the interesting code
│   └── sudoku_solver.py    # the "guts" of the app
└── tests                   # folder containing pytest unit tests
```

## Requirements

- If you want to run the pytest unit tests, you will need to install pytest. You can do this by running `pip install -r requirements-dev.txt`

## Running the Code

To solve one of the supplied sudoku puzzles, run the code as follows:

``` bash
python solve.py ./puzzles/puzzle-1-grid.txt
```

## Puzzle File Format

If you want to define a sudoku puzzle to solve, you need to save the grid to a file.

The format is pretty simple. It's 9 rows of text, with 9 digits per row. For unknown/empty cells in the grid, use a `0`.

For example, here's the contents of `puzzles/puzzle-1-grid.txt`:

``` text
047850000
900023050
005000367
008174239
000608000
104092800
461000900
070940003
000065740
```

## How the Code Works

The concept it pretty simple:

1. Try a number from 1 to 9 in the next empty space in the grid.
2. If that number fits, go on to the next empty cell and do the same thing.
3. If that number doesn't fit, try the next number until you find one that fits.
4. If you can't find any number that fits, go back (back-track) to the last empty cell and try the next number.
5. Keep backtracking, and trying numbers, until you find numbers that fit.
6. When you get to the end of the grid, then you're done!

The code here uses a concept called [Backtracking](https://en.wikipedia.org/wiki/Backtracking) to try values in the grid, and backtrack when those values fail to provide a valid solution.

Within the code, there are two functions that do all of the "interesting" work:

### The `solve_grid` function

```python
def solve_grid(grid)
```

The function `solve_grid` takes a grid (an array of arrays, loaded by `load_grid`) and solves it.
This is the function that implements the back-tracking, and calls itself recursively. 
The `solve_grid` function calls `is_valid_solution` to deterimine if a number can be placed in the grid.

### The `is_valid_solution` function

```python
def is_valid_solution(grid, row, col, solution):
```

This function takes a grid, the row and column in that grid, and a potential solution (a number from 1 to 9), and
determine if that potential solution is valid within that position in the grid.

## A Worked Example

Take this example grid. This is a 9x9 sudoku grid, where empty/unknown cells are represented by `0`.
You can find this file in the file `puzzles\puzzle-1-grid.txt`.

``` text
047850000
900023050
005000367
008174239
000608000
104092800
461000900
070940003
000065740
```
