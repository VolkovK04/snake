from threading import Thread
from classes.game import Game
from classes.snake import Direction
import socket as sock
import time
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..\\classes"))  # ???

DEBUG = True

MAX_CLIENTS = 10

CONNECTION_AWAITING = 10
FRAME_TIME = 0.1  # second

STOP_SERVER = False


class Server:

    def __init__(self) -> None:
        self._Host = sock.gethostbyname(sock.gethostname())
        self._Port = 9090

        self.s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        self.s.bind((self._Host, self._Port))

        self.s.listen(MAX_CLIENTS)

        self.active_connections: list[tuple[sock.socket, sock._RetAddress]] = []
        self.all_connections: list[tuple[sock.socket, sock._RetAddress]] = []
        self.client_threads: list[Thread] = []

    def get_conn(self):
        while True: 
            client_socket, addr = self.s.accept()

            self.all_connections.append((client_socket, addr))
            self.client_threads.append(Thread(target=self.handle_client, args=(client_socket, addr)))
            # поток на обработку сообщений от клиентов и отправку данных (хэндлер)

    def run_server(self):
        connections_thread = Thread(target=self.get_conn)
        connections_thread.start()

        time.sleep(CONNECTION_AWAITING)

        self.active_connections = self.all_connections.copy()

        self.game = Game(len(self.active_connections))
        self.game.start()
        self.send_id()
        
        self.send_game_field()

        for client_thread in self.client_threads:
            client_thread.start()

        # сервер отправляет карту клиентам
        while not STOP_SERVER:
            # фрейм игры
            self.game.update()
            self.send_game_field()
            time.sleep(FRAME_TIME)

    def handle_client(self, clientsocket: sock.socket, address):
        # сервер получает данные с клиентов и обрабатывает их
        while True:
            data = clientsocket.recv(1024).decode("utf-8")  # id move_direction
            if data:
                print(data)
                player_id, move_direction = data.split()
                self.game.snakes[int(player_id)].change_direction(Direction(int(move_direction)))

            # print(f"Data recieved from {address}:", data)

    def send_game_field(self):
        data = self.game.map_to_bytes()
        #print(self.game.map_to_string())
        #print(f"call send_game_field: data = {data}") if DEBUG else None

        for connection in self.active_connections:
            client_socket, addr = connection
            client_socket.sendall(data)

    def send_id(self):
        snakes_id = list(self.game.snakes.keys())
        for i in range(len(snakes_id)):
            clientsocket = self.active_connections[i][0]
            byte_id = str(snakes_id[i]).encode("utf-8")
            clientsocket.sendall(byte_id)


if __name__ == "__main__":
    server = Server()
    print("HOST: ", server._Host)
    server.run_server()
