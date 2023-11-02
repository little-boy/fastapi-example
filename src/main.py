from fastapi import FastAPI
import psycopg2
import sys

sys.stdout.flush()

# We connect to the database (Postgres) with :
# - psycopg2 package
# - infos coming from the setup we did in docker-compose.yml
# http://bdd:5432
conn = psycopg2.connect(
    host="bdd",
    port="5432",
    database="john",
    user="john",
    password="example"
)

app = FastAPI()

# Here is defined a route to the book listing
# We call it with (GET) http://localhost:8000/books
@app.get("/books")
def list_books():
    # Simple & concise implementation of fetching "books" from database
    cur = conn.cursor()
    cur.execute('SELECT * FROM books')
    books = cur.fetchall()
    cur.close()

    # We return books, without any kind of formatting.
    return books

