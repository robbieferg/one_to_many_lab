from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository

def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = Author(result['first_name'], result['last_name'], result['id'])
    return author