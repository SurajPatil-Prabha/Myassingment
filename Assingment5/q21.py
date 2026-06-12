class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

l = Library()
l.add_book("Python")
print(l.books)