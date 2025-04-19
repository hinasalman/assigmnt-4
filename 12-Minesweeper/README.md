# Minesweeper Game by Hina

This is a command-line implementation of the classic Minesweeper game built in Python.

## Key Features

1. **Interactive Command-Line Interface**: Play the game directly in your terminal with simple row,column inputs.
2. **Customizable Board Size**: You can adjust the board dimensions and number of bombs.
3. **Recursive Clearing**: When you dig at a location with no neighboring bombs, the game automatically clears adjacent cells.
4. **Visual Board Display**: The game provides a clear visual representation of the board with proper formatting.
5. **Game State Tracking**: The game keeps track of dug locations and determines win/loss conditions.

## Functions and Implementation

### Board Class

The game is built around a `Board` class with the following key methods:

1. `__init__(dim_size, num_bombs)`: Initializes the board with specified dimensions and number of bombs.
2. `make_new_board()`: Creates a new board and randomly plants bombs.
3. `assign_values_to_board()`: Assigns numbers to each cell representing neighboring bombs.
4. `get_num_neighboring_bombs(row, col)`: Calculates how many bombs are adjacent to a given cell.
5. `dig(row, col)`: Handles the digging action, including recursive digging for empty spaces.
6. `__str__()`: Provides a string representation of the board for display.

### Game Logic

The `play()` function controls the game flow:

1. Creates a new board
2. Shows the board to the player
3. Takes input for where to dig
4. Processes the dig action and updates the game state
5. Repeats until the player either wins or loses
6. Displays the appropriate end-game message

## Libraries Used

- `random`: Used for randomly placing bombs on the board
- `re`: Used for parsing user input with regular expressions

## How to Play

1. Run the script: `python board.py`
2. The game will display an empty board
3. Enter coordinates as "row,col" (e.g., "3,4")
4. Continue digging until you either reveal all non-bomb cells (win) or hit a bomb (lose)

## Game Rules

- Numbers indicate how many bombs are in the adjacent cells
- If you dig on a bomb, you lose
- If you reveal all non-bomb cells, you win
- Empty cells (with no neighboring bombs) will automatically reveal adjacent cells

Enjoy the game!
