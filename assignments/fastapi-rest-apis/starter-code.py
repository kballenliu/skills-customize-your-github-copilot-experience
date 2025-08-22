# FastAPI Book Library API - Starter Code

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Book Library API",
    description="A simple REST API for managing a book library",
    version="1.0.0"
)

# Pydantic models for data validation
class Book(BaseModel):
    id: int
    title: str
    author: str
    publication_year: int
    isbn: Optional[str] = None
    pages: Optional[int] = None

class BookCreate(BaseModel):
    title: str
    author: str
    publication_year: int
    isbn: Optional[str] = None
    pages: Optional[int] = None

# In-memory storage (replace with database in production)
books_db = [
    Book(id=1, title="The Python Programming Language", author="Guido van Rossum", publication_year=1991),
    Book(id=2, title="Clean Code", author="Robert C. Martin", publication_year=2008),
    Book(id=3, title="The Pragmatic Programmer", author="Andy Hunt", publication_year=1999)
]

# TODO: Implement the following endpoints:

@app.get("/")
async def root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Book Library API!"}

# TODO: GET /books - Get all books
@app.get("/books")
async def get_books():
    # Your code here
    pass

# TODO: GET /books/{book_id} - Get a specific book
@app.get("/books/{book_id}")
async def get_book(book_id: int):
    # Your code here
    pass

# TODO: POST /books - Create a new book
@app.post("/books")
async def create_book(book: BookCreate):
    # Your code here
    pass

# TODO: PUT /books/{book_id} - Update a book
@app.put("/books/{book_id}")
async def update_book(book_id: int, book: BookCreate):
    # Your code here
    pass

# TODO: DELETE /books/{book_id} - Delete a book
@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    # Your code here
    pass

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
