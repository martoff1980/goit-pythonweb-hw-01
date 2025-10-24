import logging
from abc import ABC, abstractmethod

# Налаштування логування
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


# SRP — Клас, що описує книгу
class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


# ISP — Інтерфейс для бібліотечних дій
# LSP — Усе, що реалізує цей інтерфейс, можна замінити
class LibraryInterface(ABC):

    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def get_books(self) -> list:
        pass


#  SRP — Клас бібліотеки займається тільки зберіганням книг
#  OCP — можна розширити поведінку (напр., додати сортування), не змінюючи цей код
class Library(LibraryInterface):
    def __init__(self):
        self._books: list[Book] = []

    def add_book(self, book: Book):
        self._books.append(book)

    def remove_book(self, title: str):
        self._books = [book for book in self._books if book.title != title]

    def get_books(self) -> list:
        return self._books


#  DIP — менеджер залежить не від конкретного класу Library,
# а від абстракції LibraryInterface
class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: str):
        book = Book(title, author, year)
        self.library.add_book(book)
        logging.info(f"Book '{title}' added successfully.")

    def remove_book(self, title: str):
        initial_count = len(self.library.get_books())
        self.library.remove_book(title)
        final_count = len(self.library.get_books())
        if final_count < initial_count:
            logging.info(f"Book '{title}' removed successfully.")
        else:
            logging.info(f"Book '{title}' not found.")

    def show_books(self):
        books = self.library.get_books()
        if not books:
            logging.info("No books in the library.")
        else:
            for book in books:
                logging.info(book)

        logging.info("Show command executed.")


# Головна функція (з інтерфейсом командного рядка)
def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)

            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)

            case "show":
                manager.show_books()

            case "exit":
                break

            case _:
                logging.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
