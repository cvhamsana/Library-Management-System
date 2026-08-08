from datetime import datetime

from book import Book
from member import Member
from file_handler import FileHandler


class Library:

    def __init__(self):

        self.books = []
        self.members = []
        self.transactions = []

        self.load_data()

    # -------------------------
    # LOAD DATA
    # -------------------------

    def load_data(self):

        books = FileHandler.load_data("books.json")
        members = FileHandler.load_data("members.json")
        transactions = FileHandler.load_data("transactions.json")

        self.books = [
            Book.from_dict(book)
            for book in books
        ]

        self.members = [
            Member.from_dict(member)
            for member in members
        ]

        self.transactions = transactions

    # -------------------------
    # SAVE DATA
    # -------------------------

    def save_data(self):

        FileHandler.save_data(
            "books.json",
            [book.to_dict() for book in self.books]
        )

        FileHandler.save_data(
            "members.json",
            [member.to_dict() for member in self.members]
        )

        FileHandler.save_data(
            "transactions.json",
            self.transactions
        )

    # -------------------------
    # FIND BOOK
    # -------------------------

    def find_book(self, book_id):

        for book in self.books:

            if book.book_id == book_id:
                return book

        return None

    # -------------------------
    # FIND MEMBER
    # -------------------------

    def find_member(self, member_id):

        for member in self.members:

            if member.member_id == member_id:
                return member

        return None

    # -------------------------
    # ADD BOOK
    # -------------------------

    def add_book(
        self,
        book_id,
        title,
        author,
        isbn,
        category
    ):

        if self.find_book(book_id):
            raise ValueError("Book ID already exists.")

        book = Book(
            book_id,
            title,
            author,
            isbn,
            category
        )

        self.books.append(book)

        self.save_data()

    # -------------------------
    # DELETE BOOK
    # -------------------------

    def delete_book(self, book_id):

        book = self.find_book(book_id)

        if not book:
            raise ValueError("Book not found.")

        if not book.available:
            raise ValueError(
                "Cannot delete an issued book."
            )

        self.books.remove(book)

        self.save_data()

    # -------------------------
    # ADD MEMBER
    # -------------------------

    def add_member(
        self,
        member_id,
        name,
        email,
        phone
    ):

        if self.find_member(member_id):
            raise ValueError(
                "Member ID already exists."
            )

        member = Member(
            member_id,
            name,
            email,
            phone
        )

        self.members.append(member)

        self.save_data()

    # -------------------------
    # DELETE MEMBER
    # -------------------------

    def delete_member(self, member_id):

        member = self.find_member(member_id)

        if not member:
            raise ValueError(
                "Member not found."
            )

        self.members.remove(member)

        self.save_data()

    # -------------------------
    # ISSUE BOOK
    # -------------------------

    def issue_book(
        self,
        book_id,
        member_id
    ):

        book = self.find_book(book_id)

        member = self.find_member(member_id)

        if not book:
            raise ValueError(
                "Book not found."
            )

        if not member:
            raise ValueError(
                "Member not found."
            )

        if not book.available:
            raise ValueError(
                "Book is already issued."
            )

        transaction = {

            "transaction_id":
                f"T{len(self.transactions) + 1:04}",

            "book_id": book_id,

            "member_id": member_id,

            "issue_date":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

            "return_date": "",

            "status": "Issued"
        }

        self.transactions.append(transaction)

        book.available = False

        self.save_data()

    # -------------------------
    # RETURN BOOK
    # -------------------------

    def return_book(self, book_id):

        book = self.find_book(book_id)

        if not book:
            raise ValueError(
                "Book not found."
            )

        if book.available:
            raise ValueError(
                "Book is not currently issued."
            )

        for transaction in reversed(
            self.transactions
        ):

            if (
                transaction["book_id"] == book_id
                and transaction["status"] == "Issued"
            ):

                transaction["return_date"] = (
                    datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                )

                transaction["status"] = "Returned"

                book.available = True

                self.save_data()

                return

        raise ValueError(
            "Transaction not found."
        )