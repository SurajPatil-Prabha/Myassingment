class Book:
    library_name = "City Library"

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def display_book_info(self):
        print("\nBook ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Library:", Book.library_name)

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name


book1 = Book(1, "Python Basics", "John")
book2 = Book(2, "Data Science", "David")
book3 = Book(3, "Machine Learning", "Andrew")



Book.change_library_name("Central Library")


book1.display_book_info()
book2.display_book_info()
book3.display_book_info()