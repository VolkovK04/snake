from classes.point import Point
from classes.snake import Snake, Direction
from classes.cell import Cell
from classes.gameRules import GameRules
from random import randrange


class Game:
    def __init__(self, snakes_count: int) -> None:
        self.snakes: dict[int, Snake] = {}
        self.snakes_count = snakes_count
        self.map = []
        self.game_rules = GameRules()

    def start(self) -> None:
        self.map = [[Cell.Empty for _ in range(self.game_rules.map_size)] for _ in range(self.game_rules.map_size)]
        self.generate_walls()
        self.spawn_snakes()
        self.generate_food(self.game_rules.all_food_count)

    def spawn_snakes(self) -> None:
        spawn_positions = []
        for i in range(self.game_rules.map_size):
            count = 0
            for j in range(self.game_rules.map_size):
                if self.is_empty(Point(i, j)):
                    count += 1
                else:
                    count = 0
                if count == self.game_rules.snake_spawn_size + 1:
                    spawn_positions.append(Point(i, j))
                    count = 0
        for k in range(self.snakes_count):
            position = spawn_positions[randrange(len(spawn_positions))]
            spawn_positions.remove(position)
            #здесь возможно стоит сделать доп обработку
            #------------------------------------------
            snake = Snake(position, Direction.Up)
            self.fill_cell(position, Cell.Snake)
            for i in range(1, self.game_rules.snake_spawn_size):
                snake.body.append(Point(position.x, position.y - i))
                self.fill_cell(Point(position.x, position.y - i), Cell.Snake)
            self.snakes[len(self.snakes)] = snake

    def generate_food(self, count: int = 1) -> None:
        empty_cells = []
        for i in range(self.game_rules.map_size):
            for j in range(self.game_rules.map_size):
                if self.map[i][j] == Cell.Empty:
                    empty_cells.append(Point(i, j))
        for i in range(count):
            point = empty_cells[randrange(len(empty_cells))]
            self.fill_cell(point, Cell.Food)
            empty_cells.remove(point)

    def generate_walls(self) -> None:
        square_wall_count = randrange(self.game_rules.square_wall_count_max)
        straight_wall_count = randrange(self.game_rules.straight_wall_count_max)
        single_wall_count = randrange(self.game_rules.single_wall_count_max)
        for i in range(straight_wall_count):
            self.generate_straight_wall(self.game_rules.wall_size)
        for i in range(square_wall_count):
            self.generate_square_wall(self.game_rules.wall_size)
        for i in range(single_wall_count):
            self.generate_single_wall()

    def generate_single_wall(self) -> None:
        position = Point(randrange(self.game_rules.map_size), randrange(self.game_rules.map_size))
        self.fill_cell(position, Cell.Wall)

    def generate_square_wall(self, size: int) -> None:
        position = Point(randrange(self.game_rules.map_size - size + 1), randrange(self.game_rules.map_size - size + 1))
        for i in range(size):
            for j in range(size):
                self.fill_cell(Point(position.x + i, position.y + j), Cell.Wall)

    def generate_straight_wall(self, size: int) -> None:
        if randrange(2):
            position = Point(randrange(self.game_rules.map_size - size + 1), randrange(self.game_rules.map_size))
            for i in range(size):
                self.fill_cell(Point(position.x + i, position.y), Cell.Wall)
        else:
            position = Point(randrange(self.game_rules.map_size), randrange(self.game_rules.map_size - size + 1))
            for i in range(size):
                self.fill_cell(Point(position.x, position.y + i), Cell.Wall)

    def update(self) -> None:
        for snake in self.snakes.values():
            self.move_snake(snake)

    def get_cell(self, point: Point) -> Cell:
        return self.map[point.x][point.y]

    def is_empty(self, point: Point) -> bool:
        return self.get_cell(point) == Cell.Empty

    def fill_cell(self, point: Point, cell: Cell) -> None:
        self.map[point.x][point.y] = cell

    def get_next_point(self, snake: Snake) -> Point:
        head = snake.body[-1]
        match snake.direction:
            case Direction.Up:
                return Point(head.x, (head.y - 1) % self.game_rules.map_size)
            case Direction.Right:
                return Point((head.x + 1) % self.game_rules.map_size, head.y)
            case Direction.Down:
                return Point(head.x, (head.y + 1) % self.game_rules.map_size)
            case Direction.Left:
                return Point((head.x - 1) % self.game_rules.map_size, head.y)
        return head

    def move_snake(self, snake: Snake) -> None:
        next_point = self.get_next_point(snake)
        match self.get_cell(next_point):
            case Cell.Empty:
                snake.body.append(next_point)
                self.fill_cell(next_point, Cell.Snake)
                self.fill_cell(snake.body[0], Cell.Empty)
                snake.body.pop(0)
            case Cell.Food:
                snake.body.append(next_point)
                self.fill_cell(next_point, Cell.Snake)
                self.generate_food()
            case _:
                self.delete_snake(snake)
                snake.kill()

    def delete_snake(self, snake: Snake) -> None:
        for point in snake.body:
            self.fill_cell(point, Cell.Empty)

    def map_to_string(self) -> str:
        result = ""
        for i in range(self.game_rules.map_size):
            for j in range(self.game_rules.map_size):
                result += str(self.map[i][j].value)
            result += "\n"
        return result

    def map_to_bytes(self) -> bytes:
        result = []
        for i in range(self.game_rules.map_size):
            for j in range(self.game_rules.map_size):
                result.append(self.map[i][j].value)
        return bytes(result)
