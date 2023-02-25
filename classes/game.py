from player import Player


class Game:
    def __init__(self, map: list[int, int], players: list[Player]):
        self._map = map
        self.players = players

