import enum

class MoveDirections(enum.Enum):
    UPWARD = 1
    RIGHTWARD = 2
    BOTTOMWARD = 3
    LEFTWARD = 4

class Snake:
    def __init__(self, point, move_direction) -> None:
        self._Points = [point]
        self._move_direction = move_direction

    def get_next_step(self):
        match self._move_direction:
            case MoveDirections.UPWARD:
                return (self._Points[0][0], self._Points[0][1] - 1)
            
            case MoveDirections.RIGHTWARD:
                return (self._Points[0][0] + 1, self._Points[0][1])
            
            case MoveDirections.BOTTOMWARD:
                return (self._Points[0][0], self._Points[0][1] + 1)
            
            case MoveDirections.LEFTWARD:
                return (self._Points[0][0] - 1, self._Points[0][1])
            
    def change_move(self, move_direction):
        self._move_direction = move_direction

    def move(self):
        next_step = self.get_next_step()
        self._Points.insert(0, next_step)
        del self._Points[-1]

    



