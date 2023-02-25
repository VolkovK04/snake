import graphics


class Food:

    def __init__(self, x, y):
        self._X = x
        self._Y = y

    def __str__(self):
        return f"Food on ({self._X}, {self._Y})"

