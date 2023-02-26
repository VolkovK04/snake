from enum import Enum
from point import Point
from snake import Snake
from threading import Timer


class Cell(Enum):
    Empty = 0
    Food = 1
    Snake = 2
    Wall = 3


MAP_SIZE = 30


class Game:
    def __init__(self, snakes: list[Snake]):
        self.map = [[Cell.Empty for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]
        self.snakes = snakes
        self.timer = Timer(function=self.update, interval=1)

    def setup(self):
        pass

    def update(self):
        for snake in self.snakes:
            self.move_snake(snake)

    def get_cell(self, point: Point) -> Cell:
        return self.map[point.x][point.y]

    def fill_cell(self, point: Point, cell: Cell):
        self.map[point.x][point.y] = cell

    def move_snake(self, snake: Snake):
        next_point = snake.get_next_point()
        match self.get_cell(next_point):
            case Cell.Empty:
                snake.body.insert(0, next_point)
                self.fill_cell(next_point, Cell.Snake)
                self.move_snake(snake)
                self.fill_cell(snake.body.pop(), Cell.Empty)
            case Cell.Food:
                snake.body.insert(0, next_point)
                self.fill_cell(next_point, Cell.Snake)
                self.move_snake(snake)
            case _:
                self.delete_snake(snake)
                snake.kill()

    def delete_snake(self, snake: Snake):
        for point in snake.body:
            self.fill_cell(point, Cell.Empty)


