from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

# connect to db
conn = psycopg2.connect(
    host="bdd",
    port="5432",
    database="john",
    user="john",
    password="example"
)

cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS public.books
(
    id uuid DEFAULT gen_random_uuid(),
    name character varying(255) COLLATE pg_catalog."default"
);
""")
cur.close()

app = FastAPI()

@app.get("/")
def index():
    print('HIT')

    # We return books, without any kind of formatting.
    return ['book 1', 'book 2', 'book 3']

class Book(BaseModel):
    name: str

@app.post("/books")
def create_book(book: Book):
    # -> insert item into db
    cur = conn.cursor()
    cur.execute('INSERT INTO books (name) VALUES (%s)', (book.name,))
    conn.commit()
    cur.close()

    return 'OK'

@app.get("/books")
def list_books():
    # -> select items from db
    cur = conn.cursor()
    cur.execute('SELECT * FROM books')
    books = cur.fetchall()
    cur.close()

    return books
