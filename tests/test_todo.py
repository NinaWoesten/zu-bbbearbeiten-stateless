import unittest
#Funktionen aus helper.py importieren
from helper import add, get_all, get, delete_all, update

class TestTodo(unittest.TestCase):

    def test_add(self):
        #todo hinzufügen
        add("Bis 3.09 abgeben")
        todos = get_all()
        self.assertEqual(todos[0].text, "Bbbis 3.09 abbbgebbben")
        self.assertFalse(todos[0].isCompleted)
    
    def test_get_all(self):
        add("Für Test lernen")
        add("Koffer packen")
        add("Kochen")
        todos = get_all()
        self.assertEqual(todos[0].text, "Für Test lernen")
        self.assertEqual(todos[1].text, "Koffer packen")
        self.assertEqual(todos[2].text, "Kochen")
    
    def test_get(self):
        add("Für Test lernen")
        add("Koffer packen")
        add("Kochen")
        self.assertEqual(get(0).text, "Für Test lernen")
        self.assertEqual(get(1).text, "Koffer packen")
        self.assertEqual(get(2).text, "Kochen")
    
    def test_update(self):
        add("Bis 3.09 abgeben")
        #update Funktion ausführen
        update(0)
        self.assertTrue(get(0).isCompleted)

    def test_delete(self):
        add("Für Test lernen")
        add("Koffer packen")
        add("Kochen")
        #delete Funktion aufrufen
        delete_all()
        todos = get_all()
        self.assertEqual(len(todos), 0)

if __name__ == '__main__':
    unittest.main()