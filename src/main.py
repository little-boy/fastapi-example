from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    print('HIT')

    # We return books, without any kind of formatting.
    return ['book 1', 'book 2', 'book 3']

@app.post("/books")
def create_book():
    return 'book_created'

@app.get("/books")
def list_books():
    return 'book list'