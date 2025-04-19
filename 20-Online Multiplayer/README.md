# Multiplayer Game using Pygame

## Project Files

The project consists of four Python files:

1. **server.py** - The game server that manages connections and game state.
2. **client.py** - The game client that players run to connect to the server.
3. **network.py** - Handles network communication between client and server.
4. **player.py** - Defines the Player class used by both client and server.

---

## How to Run the Game

### Step 1: Install Dependencies

Ensure you have Pygame installed. If not, install it using:

```sh
pip install pygame
```

### Step 2: Start the Server

First, you need to start the server. Open a terminal or command prompt, navigate to the project folder, and run:

```sh
python server.py
```

You should see a message saying **"Server started"** and **"Waiting for connections..."**.

### Step 3: Start the Clients

Next, open one or more additional terminals or command prompts, navigate to the project folder, and run:

```sh
python client.py
```

You can run this command in multiple terminals to have multiple players join the game.

### Step 4: Play the Game

- Use the arrow keys (**↑, ↓, ←, →**) or **W, A, S, D** to move your player.
- You will see other connected players moving in real-time.
- The game window will close if you disconnect from the server.

---

## What Each File Does

### **player.py**

This file defines the **Player** class that represents each player in the game.

- Stores the player's position (**x, y**), size, and color.
- Handles player movement based on key presses.
- Ensures players stay within the game window.
- Provides a method to draw the player on the screen.

### **network.py**

This file handles all network communication between the client and server.

- Creates a socket connection to the server.
- Sends player data to the server.
- Receives updated game state from the server.
- Uses **pickle** to convert Python objects to bytes for sending over the network.

### **server.py**

This file runs the game server that all clients connect to.

- Creates a socket server that listens for connections.
- Accepts connections from clients (players).
- Assigns each client a player ID.
- Creates a new thread to handle each client.
- Receives player movements from clients.
- Updates the game state.
- Sends the updated game state to all clients.
- Handles client disconnections.

### **client.py**

This file is the main game client that players run.

- Initializes **Pygame** and creates a game window.
- Connects to the server.
- Gets a player ID from the server.
- Creates a local player object.
- Handles player input (key presses).
- Sends the player's position to the server.
- Receives updated positions of all players.
- Draws all players on the screen.

---

## Game Controls

- **Up Arrow** or **W**: Move up
- **Down Arrow** or **S**: Move down
- **Left Arrow** or **A**: Move left
- **Right Arrow** or **D**: Move right
- **Close Window**: Quit the game

---

## Troubleshooting

### **Server Won't Start**

If you see an error like **"Address already in use"**:

1. Wait a few moments and try again.
2. Or, edit `server.py` to use a different port number.

### **Can't Connect to Server**

If the client can't connect to the server:

1. Make sure the server is running.
2. Check that you're using the correct server address.
3. Ensure your firewall isn't blocking the connection.

### **Game Lag**

This is a simple implementation without lag compensation. Some network delay is normal.

---

## Extending the Game

You can extend this basic framework by adding:

1. Game mechanics (scoring, objectives).
2. Collision detection.
3. More players.
4. Different player types or abilities.
5. Game rooms for multiple concurrent games.
6. Chat functionality.
7. Better graphics with sprites and animations.
