from flask import Flask, render_template, request, redirect
from repositories import author_repository
from repositories import book_repository

from flask import Blueprint

library_blueprint = Blueprint("library", __name__)

@library_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books = books)