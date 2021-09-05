import threading
import time


class TimeNotifier:
    def __init__(self):
        self._subscribers = []
        self._paused = False
        self._thread = threading.Thread(target=self._notify_loop)
        self._thread.setDaemon(True)
        self._thread.start()

    def _notify_loop(self):
        while True:
            if self._paused:
                continue
            for subscriber in self._subscribers:
                subscriber.update_next_second()
            time.sleep(1)

    def subscribe(self, element):
        self._subscribers.append(element)

    def toggle(self):
        self._paused = not self._paused
