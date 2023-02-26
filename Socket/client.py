import socket as sock


class Client:
    def __init__(self, server_host, server_port) -> None:
        self.s = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        self._Server_host = server_host
        self._Server_port = server_port
        
    def connect(self):
        self.s.connect((self._Server_host, self._Server_port))

    def on_snake_change_direction(self):
        data_to_send = "snake moved".encode("utf-8")
        self.s.send(data_to_send)

    def handle_data(self):
        data = self.s.recv(1024).decode("utf-8") #game_field
        #----------------------
        #что-то делаем с данными
        #----------------------
        print("Data recieved:", data)






