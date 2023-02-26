import client

HOST = input("Host: ")
PORT = int(input("Port: "))

cl = client.Client(HOST, PORT)
cl.connect()

while True:
    cl.on_snake_change_direction()
    cl.handle_data()