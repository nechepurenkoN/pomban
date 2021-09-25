from PyQt5 import QtWidgets

from gui.common import ListWidget
from model.todo import Todo
from service.mediator import Mediator

mediator = Mediator()


class DoingListWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self._main_layout = QtWidgets.QGridLayout()
        self.setLayout(self._main_layout)
        self._todo_list = ListWidget()
        self._main_layout.addWidget(self._todo_list)
        self.setStyleSheet("border: 1px solid red")
        mediator.set_doing_widget(self)

    def push_todo(self, todo: Todo):
        self._todo_list.push_todo(todo)

    def update_next_second(self):
        pass
