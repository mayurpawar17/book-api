# from fastapi import FastAPI

# app = FastAPI()

# Books = [
#     {"id": 1, "title": "1984", "author": "George Orwell"},
#     {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
# ]

# @app.get("/")
# async def read_root():
#     return {"message": "Hello from FastAPI!"}

# @app.get("/books")
# async def read_books():
#     return Books

# @app.get("/books/{book_id}")
# async def read_book(book_id: int):
#     for book in Books:
#         if book["id"] == book_id:
#             return book
#     return {"error": "Book not found"}



# @app.post("/books")
# async def create_book(book: dict):
#     new_id = max(book["id"] for book in Books) + 1 if Books else 1
#     book["id"] = new_id
#     Books.append(book)
#     return book





from fastapi import FastAPI

from app.modules.books.router import router as books_router

app = FastAPI(
    title="Book API",
    version="1.0.0",
)


app.include_router(
    books_router,
    prefix="/api/v1/books",
    tags=["Books"],
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }