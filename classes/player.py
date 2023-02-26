from snake import Snake


class Player:
    def __init__(self, snake: Snake, id: int):
        self.snake = snake
        self.id = id
