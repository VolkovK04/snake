from server.server import Server

if __name__ == "__main__":
    server = Server()
    print("HOST: ", server.host)
    server.run_server()
