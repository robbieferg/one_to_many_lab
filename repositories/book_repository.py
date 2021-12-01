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

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], result['genre'], author, result['page_count'], result['completed'], result['id'])
    return book


def save(book):
    sql = "INSERT INTO books (title, genre, author_id, page_count, completed) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [book.title, book.genre, book.author.id, book.page_count, book.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)