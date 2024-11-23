from Library.BookManager import Book
from Library.Validation import Validation


class SearchBook(Book):
    '''
    Класс для удаления книг и поиска
    '''
    def search_book(self, key, value):
        '''
        Базовый метод для поиска книги по заданному ключу и значению
        :param key: Ключ для поиска например: title. year. author
        :param value: значение для поиска например: название, год, автор
        '''

        found = False # переменная для отслеживания нахождения книги
        for book in self._books:
            if book[key] == value:
                print(book)
                found = True
        if not found:
            print(f'Книги с таким {key}, не существует\n\n')

    def search_book_title(self):
        '''
        Метод для поиска книги по названию
        :return:
        '''
        self.search_json()
        if self.message():
            return
        title = input('Введите навание: ').lower()
        self.search_book('title', title)

    def search_book_author(self):
        '''
        Метод для поиска книги по автору
        :return:
        '''
        self.search_json()
        if self.message():
            return
        author = input('Введите автора: ')
        self.search_book('author', author.title())

    def search_book_year(self):
        '''
        Метод для поиска книги по году издания
        :return:
        '''
        self.search_json()
        if self.message():
            return
        year = input('Введите год издания: ').strip()
        if not Validation.date_check(year):
            return
        year = int(year)
        self.search_book('year', year)

    def delete_book(self):
        """Удаляет книгу по ID."""
        self.search_json()
        if self.message():
            return
        book_id = input("Введите ID книги для удаления: ")
        if not book_id.isdigit():
            print('ID состоит из цифр, введите правильный ID')
            return
        book_id = int(book_id)
        for book in self._books:
            if book['id'] == book_id:
                self._books.remove(book)
                self.save_books()
                print(f"Книга с ID {book_id} удалена.\n\n")
                return
        print(f"Книга с ID {book_id} не найдена.\n\n")


