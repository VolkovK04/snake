import socket, asyncio
import time
import threading


def get_conn(serv: socket.socket):
    return serv.accept()


def listen_thread(serv):
    threading.Thread(target=get_conn, args=(serv, ))


async def main():
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 9090
 
    print("HOST:", HOST)
    print("PORT:", PORT)

    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((HOST, PORT))

    serv.listen(10)
    timeout = time.time() + 1

    conns = []
    while time.time() <= timeout:
        print(time.time())
        conns.append(get_conn(serv))

    print(conns)

asyncio.run(main())
