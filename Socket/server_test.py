import server

serv = server.Server()
serv.run_server()

while True:
    serv.send_game_field()