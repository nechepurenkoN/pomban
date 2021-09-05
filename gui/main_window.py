from PyQt5 import QtWidgets

from gui.doing import DoingListWidget
from gui.done import DoneListWidget
from gui.session import SessionSectionWidget
from gui.todo import TodoListWidget
from service.time_notifier import TimeNotifier


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
