import socket


def display_board(board):
    """Display the Tic-Tac-Toe board in a user-friendly format."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def start_client():
    """Start the client and connect to the server."""
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ("127.0.0.1", 5555)
        print(f"Connecting to server at {server_address[0]}:{server_address[1]}...")
        client.connect(server_address)
        
        # Receive player symbol (X or O)
        player = client.recv(1024).decode()
        print(f"You are Player {player}")
        
        while True:
            # Receive data from server
            data = client.recv(1024).decode()
            
            # Check if it's a special message
            if "wins" in data or "draw" in data:
                print(data)
                print("Game over! Starting a new game...")
                continue
            elif "Waiting" in data:
                print(data)
                continue
            
            # It's a board update
            board = data.split(",")
            display_board(board)
            
            # Check if it's this player's turn
            current_player = "X" if board.count("X") == board.count("O") else "O"
            if current_player == player:
                print("It's your turn!")
                valid_move = False
                while not valid_move:
                    try:
                        # Show available positions
                        available = [str(i) for i, val in enumerate(board) if val == " "]
                        print(f"Available positions: {', '.join(available)}")
                        
                        # Get player move
                        move = input("Enter your move (0-8): ")
                        if move not in available:
                            print("Invalid move! Position already taken or out of range.")
                            continue
                        
                        client.send(move.encode())
                        valid_move = True
                    except ValueError:
                        print("Please enter a number between 0 and 8.")
            else:
                print(f"Waiting for Player {current_player} to make a move...")
    
    except ConnectionRefusedError:
        print("Could not connect to the server. Make sure the server is running.")
    except KeyboardInterrupt:
        print("\nGame terminated by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        try:
            client.close()
        except Exception:
            pass
        print("Connection closed.")

if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    print("Board positions are numbered 0-8 as follows:")
    display_board(["0", "1", "2", "3", "4", "5", "6", "7", "8"])
    start_client()