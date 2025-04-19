# Sudoku Solver

A JavaScript implementation of a Sudoku solver using the backtracking algorithm.

## Overview

This project provides a solution for solving Sudoku puzzles using a backtracking algorithm. Backtracking is a recursive technique that incrementally builds candidates for solutions and abandons a candidate ("backtracks") as soon as it determines the candidate cannot lead to a valid solution.

## How It Works

The Sudoku solver works through the following steps:

1. Find the next empty cell in the puzzle.
2. If there are no empty cells, the puzzle is solved.
3. Try placing digits 1-9 in the empty cell.
4. For each digit, check if it's valid according to Sudoku rules:
   - No duplicate in the same row
   - No duplicate in the same column
   - No duplicate in the same 3x3 grid
5. If valid, place the digit and recursively try to solve the rest of the puzzle.
6. If the recursive call returns true, the puzzle is solved.
7. If the recursive call returns false, backtrack by resetting the cell to empty and try the next digit.
8. If no digits work, return false to trigger backtracking.

## Usage

```javascript
// Import the solver
const { solveSudoku, printBoard } = require('./sudoku-solver.js');

// Create a Sudoku board (use -1 for empty cells)
const board = [
  [3, 9, -1, -1, 5, -1, -1, -1, -1],
  [-1, -1, -1, 2, -1, -1, -1, -1, 5],
  [-1, -1, -1, 7, 1, 9, -1, 8, -1],
  [-1, 5, -1, -1, 6, 8, -1, -1, -1],
  [2, -1, 6, -1, -1, 3, -1, -1, -1],
  [-1, -1, -1, -1, -1, -1, -1, -1, 4],
  [5, -1, -1, -1, -1, -1, -1, -1, -1],
  [6, 7, -1, 1, -1, 5, -1, 4, -1],
  [1, -1, 9, -1, -1, -1, 2, -1, -1]
];

// Print the original board
console.log("Original Sudoku Board:");
printBoard(board);

// Solve the board
const solved = solveSudoku(board);

// Print the result
if (solved) {
  console.log("Solution found!");
  printBoard(board);
} else {
  console.log("This puzzle is unsolvable.");
}

