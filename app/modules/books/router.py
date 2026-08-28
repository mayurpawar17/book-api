from fastapi import APIRouter, HTTPException

from app.modules.books.repository import BookRepository
from app.modules.books.schemas import (
    BookResponse,
    CreateBookRequest,
    UpdateBookRequest,
)
from app.modules.books.service import BookService


router = APIRouter()


repository = BookRepository()
service = BookService(repository)


@router.get("/",response_model=list[BookResponse])
def get_books():
    return service.get_all_books()


@router.get("/{book_id}",response_model=BookResponse,)
def get_book(book_id: int):
    book = service.get_book(book_id)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found",
        )
    return book


@router.post(
    "/",
    response_model=BookResponse,
    status_code=201,
)
def create_book(data: CreateBookRequest):

    return service.create_book(data)


@router.patch(
    "/{book_id}",
    response_model=BookResponse,
)
def update_book(
    book_id: int,
    data: UpdateBookRequest,
):

    book = service.update_book(
        book_id,
        data,
    )

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found",
        )

    return book


@router.delete(
    "/{book_id}",
)
def delete_book(book_id: int):

    deleted = service.delete_book(book_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Book not found",
        )

    return {
        "message": "Book deleted successfully"
    }