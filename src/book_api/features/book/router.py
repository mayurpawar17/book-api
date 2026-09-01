# Book CRUD endpoints - handles HTTP requests for creating and retrieving books

from fastapi import APIRouter, Depends, status
from .schemas import BookCreate,  BookResponse
from .service import book_service

# Create an API router instance for organizing book-related endpoints
router = APIRouter()

# GET endpoint to retrieve all books from the database
@router.get("/", response_model=list[BookResponse])
def list_books():
    return book_service.get_all_books()

# POST endpoint to create a new book and return the created book with its ID
@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(payload: BookCreate):
    return book_service.create_book(payload)