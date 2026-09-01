# Database model for Book - defines the structure of a book record

from dataclasses import dataclass
from datetime import datetime

@dataclass
class BookRecord:
    """Data model representing a book in the database"""
    id: int                    # Unique identifier for the book
    title: str                 # Name of the book
    author: str                # Author of the book
    price: float               # Price of the book
    stock_count: int           # Number of books available in stock
    created_at: datetime       # Timestamp when the book was added