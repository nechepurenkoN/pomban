import logging
import threading
import time

from PyQt5 import QtWidgets


def to_time_string(time_value: int) -> str:
    to_watch_format = lambda unit: f"0{unit}" if unit < 10 else str(unit)
    seconds = time_value % 60
    minutes = (time_value // 60) % 60
    return f"{to_watch_format(minutes)}:{to_watch_format(seconds)}"


class SessionSectionButtons(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()


class SessionSectionWidget(QtWidgets.QWidget):
    def __init__(self, today_session: int = 1, time_on_clock: int = 1500):
        super().__init__()
        self._today_session = today_session
        self._time_on_clock = time_on_clock
        self._layout = QtWidgets.QHBoxLayout()
        self.setLayout(self._layout)
        self._label = QtWidgets.QLabel(self.__generate_label())
        self._layout.addWidget(self._label)
        self._session_buttons = SessionSectionButtons()
        self._play_btn = QtWidgets.QPushButton("Pause")
        self._play_btn = QtWidgets.QPushButton("Stop")

    def set_session_number(self, number: int):
        self._today_session = number

    def set_current_time(self, current_time: int):
        self._time_on_clock = current_time

    def update_next_second(self):
        if self._time_on_clock == 0:
            return
        self._time_on_clock -= 1
        self._label.setText(self.__generate_label())

    def __generate_label(self) -> str:
        return f"Session #{self._today_session}: {to_time_string(self._time_on_clock)}"


class TodoListWidget(QtWidgets.QWidget):
    pass


class DoingListWidget(QtWidgets.QWidget):
    def update_next_second(self):
        pass


class DoneListWidget(QtWidgets.QWidget):
    pass


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


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, time_notifier: TimeNotifier):
        super().__init__()
        self.resize(800, 500)
        self.setWindowTitle("Task list")
        self._main_widget = QtWidgets.QWidget()
        self._time_notifier = time_notifier
        self.setCentralWidget(self._main_widget)
        self._init_components()
        self._init_layouts()
        self._set_layouts()
        self._subscribe_items()

    def _init_layouts(self):
        self._grid_layout = QtWidgets.QGridLayout()

    def _set_layouts(self):
        self._main_widget.setLayout(self._grid_layout)
        self._grid_layout.addWidget(self._session_section, 0, 0, 2, 7)
        self._grid_layout.addWidget(self._todo_list, 2, 0, 8, 7)
        self._grid_layout.addWidget(self._doing_list, 0, 7, 5, 7)
        self._grid_layout.addWidget(self._done_list, 5, 7, 5, 7)

    def _init_components(self):
        self._session_section = SessionSectionWidget()
        self._todo_list = TodoListWidget()
        self._doing_list = DoingListWidget()
        self._done_list = DoneListWidget()

    def _subscribe_items(self):
        for element in (self._session_section, self._doing_list):
            self._time_notifier.subscribe(element)


def main():
    import sys
    time_notifier = TimeNotifier()
    app = QtWidgets.QApplication(sys.argv)
    with open("stylesheet/style.qss") as f:
        app.setStyleSheet("\n".join(f.readlines()))
        logging.info("Stylesheets are included")
    window = MainWindow(time_notifier)
    window.show()
    logging.info("Show main window, starting main thread")
    main_thread = threading.Thread(target=app.exec_)
    main_thread.run()


if __name__ == "__main__":
    logging_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=logging_format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Starting main...")
    main()
