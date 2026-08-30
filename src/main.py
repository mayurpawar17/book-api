from fastapi import FastAPI


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