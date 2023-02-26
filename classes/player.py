from enum import Enum
from player import Player
from point import Point
from snake import Snake


class Cell(Enum):
    Empty = 0
    Food = 1
    Snake = 2
    Wall = 3


class Game:
    def __init__(self, map: list[Cell, Cell], players: list[Player]):
        self.map = map
        self.players = players

    def next(self):
        for player in self.players:
            snake = player.snake
            new_point = snake.get_next_point()
            match self.map[new_point.x][new_point.y]:
                case Cell.Empty:
                    snake.move()
                case Cell.Food:
                    snake.move(is_food=True)
                case _:
                    self.delete_snake(snake)
                    snake.kill()

    def clear_cell(self, point: Point):
        self.map[point.x][point.y] = Cell.Empty

    def move_snake(self, snake: Snake, is_food=False):
        next_step = self.get_next_point()
        self.body.insert(0, next_step)
        if is_food:
            self.body.pop()


    def delete_snake(self, snake: Snake):
        for point in snake.body:
            self.clear_cell(point)


