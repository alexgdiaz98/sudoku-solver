# Sudoku Solver

## Explanation
Sudoku.py uses a player's logic to solve a sudoku puzzle. It looks for answers in each row, column, then section. This solution works relatively quickly.

BackTraceSudoku.py uses a greedy algorithm to solve a sudoku puzzle. It assumes the lowest possible number in each empty quare, then checks if the solution is valid. At worst, 9^81 operations. This solution is guaranteed to solve each valid puzzle.

## Usage

```./Sudoku.py```

or

```./BackTraceSudoku.py```
