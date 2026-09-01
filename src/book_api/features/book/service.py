# Business logic for books - handles creating and retrieving books
from datetime import datetime
from fastapi import HTTPException, status
from .schemas import BookCreate, BookResponse
from .models import BookRecord
from book_api.core.exceptions import ResourceNotFoundException, InvalidOperationException

# In-memory storage for books (acts as a mock database)
books_db: list[dict] = []
# Counter to generate unique IDs for new books
_id_counter: int = 1

class BookService:
    """Service class that contains all business logic for book operations"""

    def create_book(self, bookCreate: BookCreate):
        """Create a new book and add it to the in-memory database"""
        if bookCreate.price <= 0:
            raise InvalidOperationException("Book price must be greater than zero.")

        
        global _id_counter
        
        # Create a new book record with an auto-incremented ID and current timestamp
        new_book = BookRecord(
            id=_id_counter,
            title=bookCreate.title,
            author=bookCreate.author,
            price=bookCreate.price,
            stock_count=bookCreate.stock_count,
            created_at=datetime.utcnow()
        )
        
        # Store the book as a dictionary in our mock database
        books_db.append(new_book.__dict__)
        # Increment the ID counter for the next book
        _id_counter += 1
        
        # Return the created book as a response model
        return BookResponse(**new_book.__dict__)

    def get_all_books(self):
        """Retrieve all books from the database and return them as response models"""
        return [BookResponse(**book) for book in books_db]

# Create a single instance of BookService (Singleton pattern) for use throughout the app
book_service = BookService()