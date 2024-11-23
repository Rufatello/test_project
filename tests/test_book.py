import json
import unittest
from unittest.mock import patch
from Library.BookManager import Book
from io import StringIO


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book('test_library.json')

    def tearDown(self):
        try:
            with open("test_library.json", "w") as f:
                f.write("")
        except FileNotFoundError:
            pass

    def test_search_json_file_not_found(self):
        self.book.search_json()
        self.assertEqual(self.book._books, [])

    def test_search_json_file_valid(self):
        with open('test_library.json', 'w') as f:
            json.dump([{'id': 1, 'title': 'test_title', 'author': 'test_author', 'year': 2023, 'status': 'в наличии'}],
                      f)
        self.book.search_json()
        self.assertEqual(len(self.book._books), 1)

    def test_message_empty(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.book.message())
            self.assertEqual(fake_out.getvalue().strip(), 'Список книг пуст')

    def test_message_not_empty(self):
        self.book._books = [
            {'id': 1, 'title': 'test_title', 'author': 'test_author', 'year': 2023, 'status': 'в наличии'}]
        self.assertFalse(self.book.message())

    def test_save_books(self):
        self.book._books = [
            {'id': 1, 'title': 'test_title', 'author': 'test_author', 'year': 2023, 'status': 'в наличии'}]
        self.book.save_books()
        with open("test_library.json", "r", encoding='utf8') as f:
            data = json.load(f)
        self.assertEqual(data, self.book._books)

    def test_change_of_state_valid(self):
        self.book._books = [
            {"id": 1, "title": "Test Book", "author": "Test Author", "year": 2023, "status": "в наличии"}]
        with patch('builtins.input', side_effect=["1", "выдана"]):
            self.book.change_of_state()
        self.assertEqual(self.book._books[0]["status"], "выдана")

    def test_change_of_state_not_valid(self):
        self.book._books = [
            {"id": 1, "title": "Test Book", "author": "Test Author", "year": 2023, "status": "в наличии"}]
        with patch('builtins.input', side_effect=["1", "asdasd"]):
            self.book.change_of_state()
        self.assertEqual(self.book._books[0]["status"], "в наличии")
