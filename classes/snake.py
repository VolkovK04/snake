from classes.direction import Direction
from classes.point import Point


class Snake:
    def __init__(self, point: Point, direction: Direction) -> None:
        self.body = [point]
        self._direction = direction
        self.alive = True

    @property
    def direction(self) -> Direction:
        return self._direction

    def change_direction(self, new_direction: Direction) -> None:
        self._direction = new_direction

    def kill(self) -> None:
        self.alive = False

    
