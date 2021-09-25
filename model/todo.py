import uuid


class Todo:
    def __init__(self, name: str):
        self.name = name
        self.id = uuid.uuid4().hex

    def __repr__(self):
        return f"[id: {self.id}, name: {self.name}]"
