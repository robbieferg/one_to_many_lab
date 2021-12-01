from flask import Flask, render_template, request, redirect
from repositories import author_repository
from repositories import book_repository
from models.book import Book

from flask import Blueprint

library_blueprint = Blueprint("library", __name__)

@library_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books = books)

@library_blueprint.route("/books/<id>/delete", methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")

@library_blueprint.route("/books/<id>")
def show_book(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book = book)

@library_blueprint.route("/books/new")
def new_book():
    authors = author_repository.select_all()
    return render_template("/books/new.html", authors = authors)

@library_blueprint.route("/books", methods=['POST'])
def create_book():
    title = request.form['title']
    genre = request.form['genre']
    author_id = request.form['author_id']
    page_count = request.form['page_count']
    completed = request.form['completed']
    author = author_repository.select(author_id)
    book = Book(title, genre, author, page_count, completed)
    book_repository.save(book)
    return redirect("/books")