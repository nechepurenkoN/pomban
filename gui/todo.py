import logging

from PyQt5 import QtWidgets

from gui.common import ListWidget
from model.todo import Todo
from service.mediator import Mediator

mediator = Mediator()


class AddTaskWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self._main_layout = QtWidgets.QHBoxLayout()
        self.setLayout(self._main_layout)
        self._task_name_input = QtWidgets.QLineEdit()
        self._create_button = QtWidgets.QPushButton("Create")
        self._main_layout.addWidget(self._task_name_input)
        self._main_layout.addWidget(self._create_button)
        self._add_handlers()
        self.setStyleSheet("border: 1px solid red")

    def _add_handlers(self):
        self._create_button.clicked.connect(self._button_clicked)

    def _button_clicked(self):
        todo = Todo(self._task_name_input.text())
        logging.info(f"Todo created: {todo}")
        mediator.create_todo(todo)
        self._task_name_input.setText("")


class TodoListWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self._main_layout = QtWidgets.QGridLayout()
        self.setLayout(self._main_layout)
        self._add_task_widget = AddTaskWidget()
        self._todo_list = ListWidget()
        self._main_layout.addWidget(self._add_task_widget, 0, 0, 1, 1)
        self._main_layout.addWidget(self._todo_list, 1, 0, 6, 1)
        self.setStyleSheet("border: 1px solid red")
        mediator.set_todo_widget(self)

    def push_todo(self, todo: Todo):
        self._todo_list.push_todo(todo)

    def pop_todo(self, todo: Todo):
        self._todo_list.pop_todo(todo)
