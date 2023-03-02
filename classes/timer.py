from time import sleep
from threading import Thread
from event import Event


class Timer:
    def __init__(self, interval: float) -> None:
        self._interval = interval
        self.on_tick = Event()
        self._enabled = False
        self.thread = Thread(target=self.main)

    @property
    def enabled(self):
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool):
        self._enabled = value

    @property
    def interval(self):
        return self._interval

    @interval.setter
    def interval(self, value: float):
        self._interval = value

    def start(self):
        self._enabled = True
        self.thread.start()

    def stop(self):
        self._enabled = False

    def main(self):
        while self._enabled:
            self.on_tick.start()
            sleep(self.interval)
