def load_grid(file):
  """It reads from puzzle file and returns the grid values .
  :param file: It's 9 rows of text, with 9 digits per row. For unknown/empty cells in the grid, use a 0
  :type file: str
  :return: grid - the values in the cells
  :rtype: List
  """
  grid = []
  with open(file, 'r') as f:
    for line in f.readlines():
      grid_line = [int(cell) for cell in line.strip()]
      grid.append(grid_line)
  return grid

def print_grid(description, grid):
  """ It takes the grid values for Puzzle and Solution and  prints the results.

  :param description: cells in grid
  :type description: str
  :param grid: cells in grid
  :type grid: list
  :return: None - just meant to print results
  :rtype: None
  """
  print(f" {description}:")

  for counter, row in enumerate(grid):
    if counter % 3 == 0:
      print("")

    row_text = f"{grid[counter][0]}{grid[counter][1]}{grid[counter][2]} {grid[counter][3]}{grid[counter][4]}{grid[counter][5]} {grid[counter][6]}{grid[counter][7]}{grid[counter][8]}"
    print(row_text)

  print("")

def is_valid_solution(grid, row, col, solution):
  """ takes a grid, the row and column in that grid, and a potential solution (a number from 1 to 9),
   and determine if that potential solution is valid within that position in the grid.

  :param grid: cells in grid
  :type grid: list
  :param row: the number in the row
  :type row: int
  :param col:the number in col
  :type col: int
  :param solution:potential solution from 1-9
  :type solution: int
  :return: True if that solution is valid within that position in the grid
  :rtype: boolean
  """
  # check the row
  for item in grid[row]:
    if item == solution:
      return False

  # check the column
  for row_counter in range(0,9):
    if grid[row_counter][col] == solution:
      return False

  # check the squares
  grid_x = col // 3
  grid_y = row // 3

  rows_start = grid_y * 3
  rows_end = rows_start + 3

  cols_start = grid_x * 3
  cols_end = cols_start + 3

  for grid_row in range(rows_start, rows_end):
    for grid_col in range(cols_start, cols_end):
      if grid[grid_row][grid_col] == solution:
        return False

  return True

def solve_grid(grid):
  """calls is_valid_solution to deterimine if a number can be placed in the grid..
  :param grid: an array of arrays, loaded by load_grid
  :return: True if number can be placed in grid
  :rtype: boolean
  """
  for row in range(0, 9):
    for col in range(0, 9):
      if grid[row][col] == 0:
        for solution in range (1, 10):
          if is_valid_solution(grid, row, col, solution):
            grid[row][col] = solution
            solved = solve_grid(grid)
            if solved:
              return True
            else:
              grid[row][col] = 0
        return False

  return True
