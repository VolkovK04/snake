from typing import Callable


class Event:
    def __init__(self) -> None:
        self._subscribers = []

    def bind(self, action: Callable) -> None:
        self._subscribers.append(action)

    def unbind(self, action: Callable) -> None:
        self._subscribers.remove(action)

    def start(self, *args, **kwargs) -> None:
        for subscriber in self._subscribers:
            subscriber(*args, **kwargs)

