from dataclasses import dataclass

todos = []#Hier werden die Daten in einer Liste gespeichert


@dataclass
class todo:
    text: str
    isCompleted: bool = False


def add(title):
    title = title.replace('b', 'bbb').replace('B', 'Bbb')#Ver-BBB-isierung
    todos.append(todo(title))


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted
