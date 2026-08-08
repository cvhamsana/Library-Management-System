from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from library import Library


app = Flask(__name__)

app.secret_key = "library-secret-key"

library = Library()


# =========================
# DASHBOARD
# =========================

@app.route("/")
def index():

    total_books = len(library.books)

    available_books = sum(
        1
        for book in library.books
        if book.available
    )

    issued_books = (
        total_books - available_books
    )

    total_members = len(library.members)

    return render_template(
        "index.html",
        total_books=total_books,
        available_books=available_books,
        issued_books=issued_books,
        total_members=total_members
    )


# =========================
# BOOKS
# =========================

@app.route("/books")
def books():

    search = request.args.get(
        "search",
        ""
    ).lower()

    books = library.books

    if search:

        books = [
            book
            for book in books

            if search in book.title.lower()
            or search in book.author.lower()
            or search in book.book_id.lower()
            or search in book.category.lower()
        ]

    return render_template(
        "books.html",
        books=books,
        search=search
    )


# =========================
# ADD BOOK
# =========================

@app.route(
    "/add-book",
    methods=["GET", "POST"]
)
def add_book():

    if request.method == "POST":

        try:

            library.add_book(
                request.form["book_id"],
                request.form["title"],
                request.form["author"],
                request.form["isbn"],
                request.form["category"]
            )

            flash(
                "Book added successfully!",
                "success"
            )

            return redirect(
                url_for("books")
            )

        except ValueError as e:

            flash(
                str(e),
                "error"
            )

    return render_template(
        "books.html",
        books=library.books,
        search=""
    )


# =========================
# DELETE BOOK
# =========================

@app.route(
    "/delete-book/<book_id>"
)
def delete_book(book_id):

    try:

        library.delete_book(book_id)

        flash(
            "Book deleted successfully!",
            "success"
        )

    except ValueError as e:

        flash(
            str(e),
            "error"
        )

    return redirect(
        url_for("books")
    )


# =========================
# MEMBERS
# =========================

@app.route("/members")
def members():

    return render_template(
        "members.html",
        members=library.members
    )


# =========================
# ADD MEMBER
# =========================

@app.route(
    "/add-member",
    methods=["GET", "POST"]
)
def add_member():

    if request.method == "POST":

        try:

            library.add_member(
                request.form["member_id"],
                request.form["name"],
                request.form["email"],
                request.form["phone"]
            )

            flash(
                "Member added successfully!",
                "success"
            )

            return redirect(
                url_for("members")
            )

        except ValueError as e:

            flash(
                str(e),
                "error"
            )

    return render_template(
        "members.html",
        members=library.members
    )


# =========================
# DELETE MEMBER
# =========================

@app.route(
    "/delete-member/<member_id>"
)
def delete_member(member_id):

    try:

        library.delete_member(member_id)

        flash(
            "Member deleted successfully!",
            "success"
        )

    except ValueError as e:

        flash(
            str(e),
            "error"
        )

    return redirect(
        url_for("members")
    )


# =========================
# ISSUE BOOK
# =========================

@app.route(
    "/issue",
    methods=["GET", "POST"]
)
def issue():

    if request.method == "POST":

        try:

            library.issue_book(
                request.form["book_id"],
                request.form["member_id"]
            )

            flash(
                "Book issued successfully!",
                "success"
            )

            return redirect(
                url_for("transactions")
            )

        except ValueError as e:

            flash(
                str(e),
                "error"
            )

    available_books = [
        book
        for book in library.books
        if book.available
    ]

    return render_template(
        "issue.html",
        books=available_books,
        members=library.members
    )


# =========================
# RETURN BOOK
# =========================

@app.route(
    "/return/<book_id>"
)
def return_book(book_id):

    try:

        library.return_book(book_id)

        flash(
            "Book returned successfully!",
            "success"
        )

    except ValueError as e:

        flash(
            str(e),
            "error"
        )

    return redirect(
        url_for("transactions")
    )


# =========================
# TRANSACTIONS
# =========================

@app.route("/transactions")
def transactions():

    return render_template(
        "transactions.html",
        transactions=library.transactions
    )


# =========================
# RUN
# =========================

if __name__ == "__main__":

    app.run(debug=True)