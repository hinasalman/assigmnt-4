from pprint import pprint


def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9): # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:
                return r, c

    return None, None  # if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False

    # for a guess to be valid, then we need to follow the sudoku rules
    # that number must not be repeated in the row, column, or 3x3 square that it appears in

    # let's start with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False # if we've repeated, then our guess is not valid!

    # now the column
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # and then the square
    row_start = (row // 3) * 3 # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)
    
    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:  # this is true if our find_next_empty function returns None, None
        return True 
    
    # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10): # range(1, 10) is 1, 2, 3, ... 9
        # step 3: check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            # step 4: then we recursively call our solver!
            if solve_sudoku(puzzle):
                return True
        
        # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
        puzzle[row][col] = -1

    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False

def print_board(board):
    """
    Prints the Sudoku board in a readable format
    """
    print("-------------------------")
    for i in range(9):
        row_str = "| "
        for j in range(9):
            cell = " " if board[i][j] == -1 else board[i][j]
            row_str += str(cell) + " "
            if (j + 1) % 3 == 0:
                row_str += "| "
        print(row_str)
        if (i + 1) % 3 == 0:
            print("-------------------------")

def copy_board(board):
    """
    Creates a deep copy of a 2D array
    """
    return [row[:] for row in board]

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    
    # Print the original board
    print("Original Sudoku Board:")
    print_board(example_board)
    
    # Create a copy to preserve the original
    board_copy = copy_board(example_board)
    
    # Solve the puzzle
    print("\nSolving...\n")
    import time
    start_time = time.time()
    solved = solve_sudoku(board_copy)
    end_time = time.time()
    
    # Print the result
    if solved:
        print("Solution found!")
        print_board(board_copy)
        print(f"Solved in {(end_time - start_time) * 1000:.2f}ms")
    else:
        print("This puzzle is unsolvable.")
    
    # Also print using pprint for comparison
    print("\nSolution using pprint:")
    pprint(board_copy)

