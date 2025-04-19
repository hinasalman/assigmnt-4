import socket
import pickle

class Network:
    def __init__(self, server="localhost", port=5555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = server
        self.port = port
        self.addr = (self.server, self.port)
        self.player_id = self.connect()
    
    def connect(self):
        """Connect to the server and get player ID"""
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except Exception:
            pass
    
    def send(self, data):
        """Send data to server and receive response"""
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(f"Socket Error: {e}")
            return None