from typing import Optional

from app.modules.books.models import Book
from app.modules.books.repository import BookRepository
from app.modules.books.schemas import (
    CreateBookRequest,
    UpdateBookRequest,
)


class BookService:

    def __init__(self, repository: BookRepository):
        self.repository = repository

    def get_all_books(self) -> list[Book]:
        return self.repository.get_all()

    def get_book(self, book_id: int) -> Optional[Book]:
        return self.repository.get_by_id(book_id)

    def create_book(self, data: CreateBookRequest) -> Book:

        books = self.repository.get_all()

        new_id = len(books) + 1

        book = Book(
            id=new_id,
            title=data.title,
            author=data.author,
            price=data.price,
        )

        return self.repository.create(book)

    def update_book(
        self,
        book_id: int,
        data: UpdateBookRequest,
    ) -> Optional[Book]:

        book = self.repository.get_by_id(book_id)

        if book is None:
            return None

        if data.title is not None:
            book.title = data.title

        if data.author is not None:
            book.author = data.author

        if data.price is not None:
            book.price = data.price

        return book

    def delete_book(self, book_id: int) -> bool:
        return self.repository.delete(book_id)