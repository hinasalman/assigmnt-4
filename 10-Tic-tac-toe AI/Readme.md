# Tic-Tac-Toe Game

## Project Description

This is a Python-based Tic-Tac-Toe game where you can play against:

- A Human player
- A Random Computer player
- A Smart Computer player (AI using Minimax algorithm)

## Key Points

### ✅ Technologies Used

- Python 3

### ✅ Files Included

- `main.py` — The main file to run the game.
- `player.py` — Contains player classes and logic.

## ✅ Classes & Their Functions

### 1. **Player (Base Class)**

- `__init__(self, letter)` — Initializes the player with letter (X or O).
- `get_move(self, game)` — Abstract method to be overridden by child classes.

### 2. **HumanPlayer (Inherits Player)**

- Allows human input.
- Validates input move.
- `get_move(self, game)` — Takes input from the user and validates it.

### 3. **RandomComputerPlayer (Inherits Player)**

- Makes random moves.
- `get_move(self, game)` — Uses `random.choice()` to select moves.

### 4. **SmartComputerPlayer (Inherits Player)**

- Uses the Minimax algorithm to make intelligent moves.
- `get_move(self, game)` — Calls `minimax()` function.
- `minimax(self, state, player)` — Recursively finds the best move.

## ✅ TicTacToe Game Class (In `main.py`)

- `__init__(self)` — Initializes an empty 3x3 board.
- `print_board(self)` — Prints the current board.
- `print_board_nums()` — Prints numbers to guide moves.
- `make_move(self, square, letter)` — Places a letter in a square.
- `winner(self, square, letter)` — Checks if the current move is a winner.
- `empty_squares(self)` — Returns if there are empty squares.
- `num_empty_squares(self)` — Returns count of empty squares.
- `available_moves(self)` — Returns list of available moves.

## ✅ Game Play Function

- `play(game, x_player, o_player, print_game=True)` — Handles the entire game loop.

## ✅ How to Run

1. Clone the repository or download both `main.py` and `player.py`.
2. Run the following command in terminal:

```bash
python main.py
```

## ✅ Key Features

- Fully interactive console-based game.
- Human vs Computer, or Computer vs Computer.
- Smart computer player with Minimax AI.
- Clear board visuals and move guides.
- Automatic winner detection or tie announcement.

## ✅ Future Improvements (Optional Suggestions)

- Add a GUI using Tkinter or PyGame.
- Allow difficulty levels (Easy/Medium/Hard).
- Store and display game scores.

---

### ✔ Created by: Hina
