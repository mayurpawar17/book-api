from typing import Optional

from app.modules.books.models import Book


# Mock database
books_db: list[Book] = [
    Book(
        id=1,
        title="Clean Code",
        author="Robert C. Martin",
        price=30.0,
    ),
    Book(
        id=2,
        title="The Pragmatic Programmer",
        author="Andrew Hunt",
        price=35.0,
    ),
]


class BookRepository:

    def get_all(self) -> list[Book]:
        return books_db

    def get_by_id(self, book_id: int) -> Optional[Book]:
        for book in books_db:
            if book.id == book_id:
                return book

        return None

    def create(self, book: Book) -> Book:
        books_db.append(book)
        return book

    def delete(self, book_id: int) -> bool:
        for book in books_db:
            if book.id == book_id:
                books_db.remove(book)
                return True

        return False