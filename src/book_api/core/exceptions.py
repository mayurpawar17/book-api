# Custom exception classes for the application
# These exceptions can be used throughout the app to handle specific error scenarios

from typing import Any
from book_api.shared.schemas import ApiResponse, ErrorDetail
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder



def register_exception_handlers(app: FastAPI):
    
    # 1. Catch Custom Domain Exceptions (e.g. ResourceNotFoundException)
    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        return JSONResponse(
            status_code=exc.status_code,
            content=jsonable_encoder(exc.response)
        )

    # 2. Catch FastAPI/Pydantic Validation Errors (422)
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        # Format the validation error into your unified ApiResponse schema
        error_response = ApiResponse[None](
            success=False,
            data=None,
            error=ErrorDetail(
                code="VALIDATION_ERROR",
                message="Input validation failed",
                details=exc.errors()  # Passes the list of location/type details
            )
        )
        
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=jsonable_encoder(error_response)
        )


# 1. Base Application Exception
class AppException(Exception):
    """Base exception for all domain-specific errors."""
    def __init__(
        self,
        code: str,
        message: str,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        details: Any | None = None,
    ):
        self.status_code = status_code
        # Construct your uniform ApiResponse model
        self.response = ApiResponse[None](
            success=False,
            data=None,
            error=ErrorDetail(
                code=code,
                message=message,
                details=details
            )
        )

# 2. Specific Feature Exceptions
class ResourceNotFoundException(AppException):
    def __init__(self, resource: str, resource_id: Any):
        super().__init__(
            code="NOT_FOUND",
            message=f"{resource} with ID '{resource_id}' was not found.",
            status_code=status.HTTP_404_NOT_FOUND
        )

class InvalidOperationException(AppException):
    def __init__(self, message: str):
        super().__init__(
            code="INVALID_OPERATION",
            message=message,
            status_code=status.HTTP_400_BAD_REQUEST
        )