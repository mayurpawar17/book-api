# Pydantic schemas for request/response validation - defines data validation rules for API

from datetime import datetime
from pydantic import BaseModel, Field

class BookBase(BaseModel):
    """Base book schema with common fields used in both requests and responses"""
    title: str = Field(..., min_length=1, max_length=255)          # Title must be 1-255 characters
    author: str = Field(..., min_length=1, max_length=255)         # Author must be 1-255 characters
    price: float = Field(..., gt=0)                                # Price must be greater than 0
    stock_count: int = Field(default=0, ge=0)                      # Stock must be 0 or positive

class BookCreate(BookBase):
    """Schema for creating a new book (inherits all fields from BookBase)"""
    pass

class BookResponse(BookBase):
    """Schema for returning book data in API responses - includes ID and creation timestamp"""
    id: int                                                        # The book's unique identifier
    created_at: datetime                                           # When the book was created