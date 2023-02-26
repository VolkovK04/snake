from threading import Thread
import socket as sock
import time

MAX_CLIENTS = 10

class MyServer:

    def __init__(self) -> None:
        self._Host = sock.gethostbyname(sock.gethostname())
        self._Port = 9090

        self.s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        self.s.bind((self._Host, self._Port))

        self.s.listen(MAX_CLIENTS)

        self.active_connections = []
        self.all_connections = []
        self.client_threads: list[Thread] = []

    def get_conn(self):
        while True: 
            clientsocket, addr = self.s.accept()

            self.all_connections.append((clientsocket, addr))
            self.client_threads.append(Thread(target=self.handle_client, args=(clientsocket, addr)))
            #поток на обработку сообщений от клиентов и отправку данных (хэндлер)


    def server_run(self):
        timeout = 3

        connections_thread = Thread(target=self.get_conn)
        connections_thread.start()

        time.sleep(timeout)
        self.active_connections = self.all_connections.copy()

        for client_thread in self.client_threads:
            client_thread.start()

        #-------------------------
        #здесь тоже игровая логика
        #-------------------------

    def handle_client(self, clientsocket: sock.socket, address):
        while True:
            data = clientsocket.recv(1024).decode("utf-8")
            #---------------------
            #сделать чтото игровое
            #---------------------



