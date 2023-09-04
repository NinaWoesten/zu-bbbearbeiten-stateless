import pytest
import helper
import datetime


def test_add():
    # Given: I want to add a to-do with a date
    title = "Lorem ipsum"
    date = "2023-09-02"

    # When: I add the item
    helper.add(title, date)

    # Then: The most recently added to-do should have a date
    todo = helper.todos[-1]
    assert isinstance(todo.date, datetime.date)
