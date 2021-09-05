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
