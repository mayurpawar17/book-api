from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference


app = FastAPI()

class Book:
    id:int
    title:str
    author:str
    description:str
    rating:float

    def __init__(self, id:int, title:str, author:str, description:str, rating:float):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


#mock data
books=[
    Book(id=1, title="Book 1", author="Author 1", description="Description 1", rating=4.5),
    Book(id=2, title="Book 2", author="Author 2", description="Description 2", rating=4.0),
    Book(id=3, title="Book 3", author="Author 3", description="Description 3", rating=4.8)
]



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/books")
def get_books():
    print(f"Getting all books {len(books)}")
    return books




@app.get("/scalar", include_in_schema=False)
async def scalar():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )