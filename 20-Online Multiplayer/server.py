import socket
import threading

# Game state
board = [" " for _ in range(9)]  # 3x3 Tic-Tac-Toe board
current_player = "X"
clients = []
lock = threading.Lock()

def handle_client(client_socket, player):
    global current_player, board
    
    # Send initial board to the client
    client_socket.send(f"{','.join(board)}".encode())
    
    while True:
        try:
            # Receive move from client
            move = client_socket.recv(1024).decode()
            if not move:
                break

            # Update game state
            with lock:
                try:
                    move_index = int(move)
                    if 0 <= move_index <= 8 and board[move_index] == " " and current_player == player:
                        board[move_index] = player
                        current_player = "O" if player == "X" else "X"
                        
                        # Send updated board to both clients
                        for c in clients:
                            c.send(f"{','.join(board)}".encode())
                        
                        # Check for win or draw
                        if check_win(board):
                            for c in clients:
                                c.send(f"Player {player} wins!".encode())
                            # Reset the board for a new game
                            board = [" " for _ in range(9)]
                            current_player = "X"
                        elif " " not in board:
                            for c in clients:
                                c.send("It's a draw!".encode())
                            # Reset the board for a new game
                            board = [" " for _ in range(9)]
                            current_player = "X"
                except ValueError:
                    # Invalid move format
                    client_socket.send(f"{','.join(board)}".encode())
                    
        except Exception as e:
            print(f"Error: {e}")
            break

    # Close connection
    print(f"Player {player} disconnected")
    if client_socket in clients:
        clients.remove(client_socket)
    client_socket.close()

def check_win(board):
    # Check rows, columns, and diagonals for a win
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return True
    return False

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", 5555))  # Bind to all interfaces on port 5555
    server.listen(2)
    print("Server started. Waiting for players...")

    try:
        while True:
            # Accept new connections until we have 2 players
            while len(clients) < 2:
                client_socket, addr = server.accept()
                print(f"Player {len(clients) + 1} connected from {addr}")
                clients.append(client_socket)

                # Assign player symbol (X or O)
                player = "X" if len(clients) == 1 else "O"
                client_socket.send(player.encode())

                # Start a thread to handle the client
                client_thread = threading.Thread(target=handle_client, args=(client_socket, player))
                client_thread.daemon = True
                client_thread.start()
                
                # If we have one player, tell them to wait
                if len(clients) == 1:
                    clients[0].send("Waiting for another player to join...".encode())
                
            # Wait for a player to disconnect before accepting new connections
            while len(clients) == 2:
                threading.Event().wait(1)
    except KeyboardInterrupt:
        print("Server shutting down...")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()