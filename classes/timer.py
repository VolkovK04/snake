from time import sleep
from threading import Thread
from event import Event


class Timer:
    def __init__(self, interval: float) -> None:
        self._interval = interval
        self.on_tick = Event()
        self._enabled = False
        self.thread = Thread(target=self._main)

    @property
    def enabled(self) -> bool:
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value

    @property
    def interval(self) -> float:
        return self._interval

    @interval.setter
    def interval(self, value: float) -> None:
        self._interval = value

    def start(self) -> None:
        self._enabled = True
        self.thread.start()

    def stop(self) -> None:
        self._enabled = False

    def _main(self) -> None:
        while self._enabled:
            self.on_tick.start()
            sleep(self.interval)
