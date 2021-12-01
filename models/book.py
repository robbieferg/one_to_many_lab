class Book:
    def __init__(self, title, genre, author, page_count, completed = False, id = None):
        self.title = title
        self.genre = genre
        self.auhtor = author
        self.page_count = page_count
        self.completed = completed
        self.id = id

    def mark_complete(self):
        self.completed = True