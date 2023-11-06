from fastapi import FastAPI
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

@app.post("/books")
def create_book():
    return 'book_created'

@app.get("/books")
def list_books():
    # -> select items from db
    cur = conn.cursor()
    cur.execute('SELECT * FROM books')
    books = cur.fetchall()
    cur.close()
    return books