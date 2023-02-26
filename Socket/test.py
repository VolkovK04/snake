from threading import Thread
import socket
import time


MAX_PLAYERS = 10


def get_conn(serv: socket.socket, connections: list):
    while True:
        connections.append(serv.accept())


def main():
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 9090

    print("HOST:", HOST)
    print("PORT:", PORT)

    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((HOST, PORT))

    serv.listen(MAX_PLAYERS)

    conns = []
    
    thread = Thread(target=get_conn, args=(serv, conns))
    thread.start()
    time.sleep(1)
    thread.join()

    print(conns)


main()



