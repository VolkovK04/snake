from threading import Thread
from classes.event import Event
import socket as sock

DEBUG = True

MAX_CLIENTS = 10


class Server:

    def __init__(self) -> None:
        self.client_connected = Event()
        """args(client_socket, address)"""
        self.client_disconnected = Event()
        """args(client_socket, address)"""
        self.message_received = Event()
        """args(client_socket, address, data)"""
        self.enabled = True

        self._host = sock.gethostbyname(sock.gethostname())
        self._port = 9090

        self.s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        self.s.bind((self._host, self._port))
        self.s.listen(MAX_CLIENTS)
        self.all_connections: list[tuple[sock.socket, sock.AddressFamily]] = []

    @property
    def host(self):
        return self._host

    def _get_connection(self):
        while self.enabled:
            client_socket, address = self.s.accept()
            self.all_connections.append((client_socket, address))
            Thread(target=self._handle_client, args=(client_socket, address)).start()
            self.client_connected.start(client_socket, address)

    def start(self) -> None:
        Thread(target=self._get_connection).start()

    def stop(self):
        self.enabled = False
        self.s.close()

    def _handle_client(self, client_socket: sock.socket, address: sock.AddressFamily):
        """сервер получает данные с клиентов и обрабатывает их"""
        while self.enabled:
            data = client_socket.recv(1024)
            if data:
                self.message_received.start(client_socket, address, data)
            if DEBUG:
                print(f"Data received from {address}:", data.decode("utf-8"))

    @staticmethod
    def send_message(connection: tuple[sock.socket, sock.AddressFamily], message: bytes):
        connection[0].sendall(message)

    def send_message_for_all(self, message: bytes):
        for connection in self.all_connections:
            self.send_message(connection, message)





