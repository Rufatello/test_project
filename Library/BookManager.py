import json

from Library.Validation import Validation


class Book:
    def __init__(self, filename="library.json"):
        '''
        Инициализация класса Book
        :param filename: Имя файла в которм будут храниться данные о книгах
        '''
        self._books = []
        self.filename = filename

    def search_json(self):
        '''
        Метод для загрузки данных о книгах
        :return:
        '''
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                file_content = f.read()
                if file_content.strip():
                    self._books = json.loads(file_content)
                else:
                    self._books = []
        except FileNotFoundError:
            self._books = []
        except json.JSONDecodeError:
            print("Ошибка: файл JSON содержит некорректные данные.")
            self._books = []

    def message(self):
        '''
        Метод для вывода сообщения, если файл пуст
        :return: True, если файл пуст, иначе False
        '''
        if not self._books:
            print('Список книг пуст\n\n')
            return True
        return False

    def add_book(self):
        '''
        Метод для добавления новой книги
        Пользователь вводит данные о новой книге и добавляет ее в список self.book
        сохраняет список в json-файл
        :return:
        '''
        next_id = len(self._books) + 1 if self._books else 1
        author = input("Введите фамилию автора (например: 'Пушкин'): ")
        title = input("Название книги: ")
        year = input("Год в формате гггг: ")
        if not Validation.date_check(year):
            return
        if not Validation.field_value(title, author):
            return
        year = int(year)
        self._books.append({"id": next_id, "author": author.title(), "title": title.lower(), "year": year,
                           "status": "в наличии"})
        print('Книга добавлена\n\n')
        self.save_books()

    def save_books(self):
        '''
        Метод для сохранения данных о книгах в json-файл
        :return:
        '''
        with open(self.filename, "w", encoding='utf-8') as file:
            json.dump(self._books, file, indent=4, ensure_ascii=False)

    def all_books(self):
        '''
        Метод для вывода всех книг
        :return:
        '''
        if self.message():
            return
        for book in self._books:
            print(book)

    def change_of_state(self):
        '''
        Метод для изменения статуса книги, пользователь вводит id ниги и новый статус
        изменяет статус книги в json-файле
        :return:
        '''
        if self.message():
            return
        try:
            book_id = int(input("Введите ID книги для изменения статуса: "))
        except ValueError:
            print("Ошибка: ID книги должно быть целым числом.\n")
            return
        for book in self._books:
            if book['id'] == book_id:
                state = input('Введите новый статус (в наличии или выдана): ').lower()
                if state.lower() == 'в наличии' or state.lower() == 'выдана':
                    book['status'] = state
                    self.save_books()
                    print(f"Статус книги с ID {book_id} изменен на '{state}'.\n")
                else:
                    print('Не может быть такого статуса\n\n')
                return
        print(f"Книга с ID {book_id} не найдена.\n\n")
