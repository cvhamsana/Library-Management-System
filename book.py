class Book:
    def __init__(self, book_id, title, author, isbn, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.category = category
        self.available = True

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "category": self.category,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        book = Book(
            data["book_id"],
            data["title"],
            data["author"],
            data["isbn"],
            data["category"]
        )

        book.available = data.get("available", True)
        return book