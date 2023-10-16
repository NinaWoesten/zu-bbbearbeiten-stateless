import unittest
#Funktionen aus helper.py importieren
from helper import add, get_all, get, delete_all, update

class TestCSVDownload(unittest.TestCase):

    def test_csv(self):
         sample_data = [
            {"title": "Item 1", "category": "Category A", "description": "Description 1"},
            {"title": "Item 2", "category": "Category B", "description": "Description 2, mit Komma},
        ]
 csv_string = get_csv(sample_data)

        self.assertTrue(csv_string)
