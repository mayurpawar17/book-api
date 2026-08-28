from typing import Optional

from pydantic import BaseModel


class CreateBookRequest(BaseModel):
    title: str
    author: str
    price: float


class UpdateBookRequest(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    price: Optional[float] = None


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    price: float