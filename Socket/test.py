from threading import Thread
import socket
import time


MAX_PLAYERS = 10


def get_conn(serv: socket.socket, connections: list, flag=True):
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
    flag = True
    thread = Thread(target=get_conn, args=(serv, conns, flag))
    thread.start()
    time.sleep(1)
    event.set()
    thread.join()

    print(conns)


main()



