class Event:
    def __init__(self):
        self.subscribers = []

    def bind(self, func):
        self.subscribers.append(func)

    def unbind(self, func):
        self.subscribers.remove(func)

    def start(self, *args, **kwargs):
        for subscriber in self.subscribers:
            subscriber(*args, **kwargs)

