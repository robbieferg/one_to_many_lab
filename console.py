import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

author_1 = Author("Stephen", "King")
author_repository.save(author_1)

author_2 = Author("J.R.R.", "Tolkien")
author_repository.save(author_2)

book_1 = Book("The Shining", "horror", author_1, 350)
book_repository.save(book_1)

book_2 = Book("The Hobbit", "fantasy", author_2, 400)
book_repository.save(book_2)

pdb.set_trace()
