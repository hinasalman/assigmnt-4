# # Author: Hina
# # Created: 6 April, 2025
# # Simple Tic-Tac-Toe Game in Python (Console-based)

# # Function to print the game board
# def print_board(board):
#     print("\n")
#     for row in board:
#         print(" | ".join(row))
#         print("-" * 9)

# # Function to check for winner
# def check_winner(board, player):
#     # Check rows, columns, and diagonals
#     for i in range(3):
#         if all([cell == player for cell in board[i]]):
#             return True
#         if all([board[j][i] == player for j in range(3)]):
#             return True

#     if all([board[i][i] == player for i in range(3)]):
#         return True

#     if all([board[i][2 - i] == player for i in range(3)]):
#         return True

#     return False

# # Function to check tie
# def check_tie(board):
#     for row in board:
#         if " " in row:
#             return False
#     return True

# # Main game loop
# def play_game():
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     current_player = "X"

#     print("\n=== Welcome to Simple Tic-Tac-Toe Game by Touseef ===")
#     print("Date: 3 April, 2025")

#     while True:
#         print_board(board)
#         print(f"Player {current_player}'s turn.")

#         try:
#             row = int(input("Enter row (0, 1, or 2): "))
#             col = int(input("Enter column (0, 1, or 2): "))
#         except ValueError:
#             print("Invalid input! Please enter numbers.")
#             continue

#         if 0 <= row <= 2 and 0 <= col <= 2:
#             if board[row][col] == " ":
#                 board[row][col] = current_player

#                 if check_winner(board, current_player):
#                     print_board(board)
#                     print(f"Congratulations! Player {current_player} wins!")
#                     break

#                 if check_tie(board):
#                     print_board(board)
#                     print("It's a tie!")
#                     break

#                 current_player = "O" if current_player == "X" else "X"
#             else:
#                 print("Cell already occupied. Try another.")
#         else:
#             print("Invalid row or column! Choose between 0 and 2.")

# if __name__ == "__main__":
#     play_game()
