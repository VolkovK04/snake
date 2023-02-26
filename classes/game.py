from enum import Enum
from point import Point
from snake import Snake, Direction
import time
from random import randrange


class Cell(Enum):
    Empty = 0
    Food = 1
    Snake = 2
    Wall = 3


MAP_SIZE = 30
WALL_SIZE = 5
FOOD_COUNT = 10
SNAKE_SPAWN_SIZE = 4


class Game:
    def __init__(self, snakes_count: int):
        self.map = [[Cell.Empty for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]
        self.snakes = []
        self.snakes_count = snakes_count

    def start(self):
        self.generate_walls()
        self.spawn_snakes()
        self.generate_food(FOOD_COUNT)

    def spawn_snakes(self):
        spawn_positions = []
        for i in range(MAP_SIZE):
            count = 0
            for j in range(MAP_SIZE):
                if self.is_empty(Point(i, j)):
                    count += 1
                else:
                    count = 0
                if count == SNAKE_SPAWN_SIZE + 1:
                    spawn_positions.append(Point(i, j))
                    count = 0
        for k in range(self.snakes_count):
            position = spawn_positions[randrange(len(spawn_positions))]
            spawn_positions.remove(position)
            snake = Snake(position, Direction.Up)
            self.fill_cell(position, Cell.Snake)
            for i in range(1, SNAKE_SPAWN_SIZE - 1):
                snake.body.append(Point(position.x, position.y - i))
                self.fill_cell(Point(position.x, position.y - i), Cell.Snake)
            self.snakes.append(snake)

    def generate_food(self, count: int = 1) -> None:
        empty_cells = []
        for i in range(MAP_SIZE):
            for j in range(MAP_SIZE):
                if self.map[i][j] == Cell.Empty:
                    empty_cells.append(Point(i, j))
        for i in range(count):
            point = empty_cells[randrange(len(empty_cells))]
            self.fill_cell(point, Cell.Food)
            empty_cells.remove(point)

    def generate_walls(self) -> None:
        straight_wall_count = randrange(10)
        square_wall_count = randrange(5)
        single_wall_count = randrange(15)
        for i in range(straight_wall_count):
            self.generate_straight_wall(WALL_SIZE)
        for i in range(square_wall_count):
            self.generate_square_wall(WALL_SIZE)
        for i in range(single_wall_count):
            self.generate_single_wall()

    def generate_single_wall(self):
        position = Point(randrange(MAP_SIZE), randrange(MAP_SIZE))
        self.fill_cell(position, Cell.Wall)

    def generate_square_wall(self, size: int) -> None:
        position = Point(randrange(MAP_SIZE - size + 1), randrange(MAP_SIZE - size + 1))
        for i in range(size):
            for j in range(size):
                self.fill_cell(Point(position.x + i, position.y + j), Cell.Wall)

    def generate_straight_wall(self, size: int):
        if randrange(2):
            position = Point(randrange(MAP_SIZE - size + 1), randrange(MAP_SIZE))
            for i in range(size):
                self.fill_cell(Point(position.x + i, position.y), Cell.Wall)
        else:
            position = Point(randrange(MAP_SIZE), randrange(MAP_SIZE - size + 1))
            for i in range(size):
                self.fill_cell(Point(position.x, position.y + i), Cell.Wall)

    def update(self):
        for snake in self.snakes:
            self.move_snake(snake)

    def get_cell(self, point: Point) -> Cell:
        return self.map[point.x][point.y]

    def is_empty(self, point: Point) -> bool:
        return self.get_cell(point) == Cell.Empty

    def fill_cell(self, point: Point, cell: Cell):
        self.map[point.x][point.y] = cell

    def move_snake(self, snake: Snake):
        next_point = snake.get_next_point()
        match self.get_cell(next_point):
            case Cell.Empty:
                snake.body.append(next_point)
                self.fill_cell(next_point, Cell.Snake)
                self.fill_cell(snake.body.pop(), Cell.Empty)
            case Cell.Food:
                snake.body.append(next_point)
                self.fill_cell(next_point, Cell.Snake)
                self.generate_food()
            case _:
                self.delete_snake(snake)
                snake.kill()

    def delete_snake(self, snake: Snake):
        for point in snake.body:
            self.fill_cell(point, Cell.Empty)

    def map_to_string(self) -> str:
        result = ""
        for i in range(MAP_SIZE):
            for j in range(MAP_SIZE):
                result += str(self.map[i][j].value)
            result += "\n"
        return result

    def map_to_bytes(self) -> bytes:
        result = []
        for i in range(MAP_SIZE):
            for j in range(MAP_SIZE):
                result.append(self.map[i][j]._value_)
        return bytes(result)
