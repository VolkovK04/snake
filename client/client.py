import socket as sock
import keyboard
from enum import Enum
import time
from graphics import GUI

MAX_SIZE_BYTES = 1024
ID_MAX_LEN = 2

FRAME_TIME = 1
STOP_CLIENT = False

class Direction(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3

class Cell(Enum):
    Empty = 0
    Food = 1
    Snake = 2
    Wall = 3




class Client:
    def __init__(self, server_host, server_port) -> None:
        self.s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        self._Server_host = server_host
        self._Server_port = server_port

        self.gui = GUI([])

        
    def connect(self):
        self.s.connect((self._Server_host, self._Server_port))

    def on_snake_change_direction(self, move_direction: Direction):
        data_to_send = f"{self._Id} {move_direction.value}".encode("utf-8")
        self.s.sendall(data_to_send)

    def handle_server(self):
        data = self.s.recv(MAX_SIZE_BYTES)
        if len(data) <= ID_MAX_LEN:
            id = int(data.decode("utf-8"))
            self._Id = id
        else:
            map = list() #game_field
            self.map_size = int(len(map)**0.5)

            self.map = [[map[i * self.map_size + j] for j in range(self.map_size)] for i in range(self.map_size)]
            self.gui.new_map = self.map

    def setup(self):
        self.connect()
        self.handle_server()
        self.gui.draw()
    
    def detect_direction(self, key):
        match key:
            case "up":
                self.on_snake_change_direction(Direction.Up)
            case "right":
                self.on_snake_change_direction(Direction.Right)
            case "down":
                self.on_snake_change_direction(Direction.Down)
            case "left":
                self.on_snake_change_direction(Direction.Left)

    def run_client(self):
        self.setup()
        while not STOP_CLIENT:
            self.handle_server()
            print("drawing")
            self.gui.draw()
            key = keyboard.read_key()
            self.detect_direction(key)
            time.sleep(FRAME_TIME)
            


if __name__ == "__main__":
    HOST = input("HOST: ")
    PORT = 9090

    client = Client(HOST, PORT)
    client.run_client()



