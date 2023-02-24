import socket
import random

HOST = socket.gethostbyname(socket.gethostname())
PORT = random.randint(5000, 10000)

print("HOST:", HOST)
print("PORT:", PORT)


serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(HOST, PORT)

serv.listen(1)

while True:
    conn, addr = serv.accept()

    data = input("Data to send: ")
    send_data = data.encode()
    conn.sendall(send_data)
    recv_data = conn.recv(1024).decode()
    print("Recieved:", recv_data)
