import logging

from PyQt5 import QtWidgets

from model.todo import Todo
from service.mediator import Mediator

mediator = Mediator()


class TodoListItem(QtWidgets.QFrame):
    def __init__(self, todo: Todo):
        super().__init__()
        self._todo = todo
        self._main_layout = QtWidgets.QHBoxLayout()
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed))
        self.setLayout(self._main_layout)
        self._name_label = QtWidgets.QLabel(f"{todo.name}")
        self._move_button = QtWidgets.QPushButton(">")
        self._move_button.clicked.connect(self._button_clicked)
        self._main_layout.addWidget(self._name_label)
        self._main_layout.addWidget(self._move_button)
        self.setStyleSheet("border: 1px solid red")

    def _button_clicked(self):
        mediator.move_to_doing(self._todo)


class ListWidget(QtWidgets.QFrame):
    def __init__(self):
        super().__init__()
        self._todos = {}
        self._main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(self._main_layout)
        self.setStyleSheet("border: 1px solid red")

    def push_todo(self, todo: Todo):
        self._todos.update({todo.id: TodoListItem(todo)})
        self._main_layout.insertWidget(0, self._todos[todo.id])
        self._main_layout.addStretch()
        self._render()

    def pop_todo(self, todo: Todo):
        self._main_layout.removeWidget(self._todos[todo.id])
        self._todos.pop(todo.id)
        self._render()

    def _render(self):
        QtWidgets.QApplication.processEvents()
        logging.info(f"Rendered: {self._todos}")
