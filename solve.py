import solver.sudoku_solver
import argparse

def main(puzzle_file_path):
  """It reads from puzzle file poth and returns the grid values .
   :param file: It's 9 rows of text, with 9 digits per row. For unknown/empty cells in the grid, use a 0
   :type file: str
   :return: None
   :rtype: None
   """
  grid = solver.sudoku_solver.load_grid(puzzle_file_path)
  solver.sudoku_solver.print_grid("Puzzle", grid)
  solved = solver.sudoku_solver.solve_grid(grid)
  solver.sudoku_solver.print_grid("Solution", grid)


parser = argparse.ArgumentParser(description='Sudoku Solver')
parser.add_argument('gridpath', metavar='FILEPATH', help='path to sudoku grid to solve')
args = parser.parse_args()

main(args.gridpath)
