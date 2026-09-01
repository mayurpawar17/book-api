from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from book_api.features.book import books_router
from book_api.core.exceptions import register_exception_handlers

# Create the FastAPI application instance with metadata
app = FastAPI(
    title="Book API (Mocked DB)",
    version="0.1.0"
)

# Register custom and validation handlers
register_exception_handlers(app)

# CORS middleware is commented out but can be enabled for cross-origin requests
# Uncomment and adjust allowed origins for production use

# Health check endpoint to verify if the API is running
@app.get("/health", tags=["System"])
def health_check():
    return {"status": "ok", "message": "Book API is running"}

# Register the books router to handle all book-related endpoints (GET /books, POST /books, etc.)
# Auth router is commented out for now but can be enabled later
app.include_router(books_router, prefix="/api/v1/books", tags=["Books"])



# Serve the Scalar API documentation UI
# Provides an alternative interactive API documentation viewer
@app.get("/scalar", include_in_schema=False)
async def scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )