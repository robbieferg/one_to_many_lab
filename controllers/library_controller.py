from flask import Flask, render_template, request, redirect
from repositories import author_repository
from repositories import book_repository

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
