from enum import Enum
from classes.point import Point


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

    def change_direction(self, new_direction):
        self.direction = new_direction

    def kill(self):
        self.alive = False

    
