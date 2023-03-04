from server.server import Server
from classes.game import Game
from time import sleep

CONNECTION_AWAITING = 10

if __name__ == "__main__":
    server = Server()
    print("HOST: ", server.host)
    server.start()
    sleep(CONNECTION_AWAITING)
    game = Game(len(server.all_connections), server)
    game.start()

