from datetime import datetime
from typing import Generic, TypeVar, Any
from pydantic import BaseModel, Field

T = TypeVar("T")

# Single Error Detail
class ErrorDetail(BaseModel):
    code: str = Field(..., example="NOT_FOUND")
    message: str = Field(..., example="The requested resource was not found.")
    details: Any | None = None  # Validation details or additional context

# Standard Unified API Envelope
class ApiResponse(BaseModel, Generic[T]):
    success: bool
    data: T | None = None
    error: ErrorDetail | None = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)