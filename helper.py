from dataclasses import dataclass
from datetime import datetime

todos = []#Hier werden die Daten in einer Liste gespeichert


@dataclass
class todo:
    title: str
    date: datetime
    isCompleted: bool = False


def add(title, date):
    title = title.replace('b', 'bbb').replace('B', 'Bbb')#Ver-BBB-isierung
    date = datetime.strptime(date, '%Y-%m-%d')
    todos.append(todo(title, date))


def get_all():
    return todos


def get(index):
    return todos[index]


def update(index):
    todos[index].isCompleted = not todos[index].isCompleted

def delete_all():
    todos.clear()