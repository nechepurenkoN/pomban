import logging

from model.todo import Todo


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Mediator:
    def __init__(self):
        self._todo_widget = None

    def set_todo_widget(self, todo_widget):
        self._todo_widget = todo_widget

    def set_doing_widget(self, doing_widget):
        self._doing_widget = doing_widget

    def create_todo(self, todo: Todo):
        self._todo_widget.push_todo(todo)
        # db.push_todo()

    def move_to_doing(self, todo: Todo):
        logging.info(f"Move {todo.id}")
        self._todo_widget.pop_todo(todo)
        self._doing_widget.push_todo(todo)
