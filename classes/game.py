import player


class Game:
    def __init__(self, map: list[int, int], players: list[player]):
        self._map = map
        self.players = players

