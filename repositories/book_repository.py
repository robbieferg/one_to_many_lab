from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], row['genre'], author, row['page_count'], row['completed'], row['id'])
        books.append(book)
    return books

def save(book):
    sql = "INSERT INTO books (title, genre, author_id, page_count, completed) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.author.id, book.page_count, book.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book