from Library.BookManager import Book
from Library.BookSearch import SearchBook

books = Book()
books.search_json()
search = SearchBook()


def main():
    while True:

        action = input(
            '''Введите действие: 
            1-Добавить книгу: 
            2-Удалить книгу: 
            3-Найти книгу по автору: 
            4-Найти книгу по названию: 
            5-Найти книгу по году издания:
            6-Вывести все книги:
            7-Изменить статус книги: 
            8-Выход: ''')
        if action == '1':
            books.add_book()
        elif action == '2':
            search.delete_book()
        elif action == "3":
            search.search_book_author()
        elif action == "4":
            search.search_book_title()
        elif action == "5":
            search.search_book_year()
        elif action == "6":
            books.all_books()
        elif action == "7":
            books.change_of_state()
        elif action == "8":
            break
        else:
            print(f'Не знаю такого "{action}" действия, пожалуйста выбери из предложенных')


if __name__ == "__main__":
    main()
