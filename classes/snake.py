from enum import Enum
from point import Point


class Direction(Enum):
    Up = 0
    Right = 1
    Down = 2
    Left = 3


class Snake:
    def __init__(self, point: Point, move_direction: Direction) -> None:
        self.body = [point]
        self.direction = move_direction
        self.alive = True

    def get_next_point(self):
        head = self.body[-1]
        match self.direction:
            case Direction.Up:
                return Point(head.x, head.y - 1)
            case Direction.Right:
                return Point(head.x + 1, head.y)
            case Direction.Down:
                return Point(head.x, head.y + 1)
            case Direction.Left:
                return Point(head.x - 1, head.y)
            
    def change_move(self, new_direction):
        self.direction = new_direction

    def kill(self):
        self.alive = False

    
