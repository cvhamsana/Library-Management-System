from library import Library


def book_menu(library):

    while True:

        print("\n")
        print("=" * 45)
        print("         BOOK MANAGEMENT")
        print("=" * 45)

        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Search Book")
        print("6. View Available Books")
        print("7. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        try:

            if choice == "1":

                book_id = input("Enter Book ID: ").strip()
                title = input("Enter Title: ").strip()
                author = input("Enter Author: ").strip()
                isbn = input("Enter ISBN: ").strip()
                category = input("Enter Category: ").strip()

                library.add_book(
                    book_id,
                    title,
                    author,
                    isbn,
                    category
                )

            elif choice == "2":

                library.view_books()

            elif choice == "3":

                book_id = input("Enter Book ID to update: ").strip()

                library.update_book(book_id)

            elif choice == "4":

                book_id = input("Enter Book ID to delete: ").strip()

                library.delete_book(book_id)

            elif choice == "5":

                keyword = input(
                    "Enter title, author, ISBN or category: "
                ).strip()

                library.search_books(keyword)

            elif choice == "6":

                library.view_available_books()

            elif choice == "7":

                break

            else:

                print("\nInvalid choice. Please try again.")

        except ValueError as error:

            print(f"\nError: {error}")

        except Exception as error:

            print(f"\nUnexpected error: {error}")


def member_menu(library):

    while True:

        print("\n")
        print("=" * 45)
        print("        MEMBER MANAGEMENT")
        print("=" * 45)

        print("1. Add Member")
        print("2. View Members")
        print("3. Update Member")
        print("4. Delete Member")
        print("5. Search Member")
        print("6. Back to Main Menu")

        choice = input("\nEnter your choice: ").strip()

        try:

            if choice == "1":

                member_id = input("Enter Member ID: ").strip()
                name = input("Enter Name: ").strip()
                email = input("Enter Email: ").strip()
                phone = input("Enter Phone: ").strip()

                library.add_member(
                    member_id,
                    name,
                    email,
                    phone
                )

            elif choice == "2":

                library.view_members()

            elif choice == "3":

                member_id = input(
                    "Enter Member ID to update: "
                ).strip()

                library.update_member(member_id)

            elif choice == "4":

                member_id = input(
                    "Enter Member ID to delete: "
                ).strip()

                library.delete_member(member_id)

            elif choice == "5":

                keyword = input(
                    "Enter member ID, name, email or phone: "
                ).strip()

                library.search_members(keyword)

            elif choice == "6":

                break

            else:

                print("\nInvalid choice. Please try again.")

        except ValueError as error:

            print(f"\nError: {error}")

        except Exception as error:

            print(f"\nUnexpected error: {error}")


def main():

    library = Library()

    while True:

        print("\n")
        print("=" * 55)
        print("           LIBRARY MANAGEMENT SYSTEM")
        print("=" * 55)

        print("1. Book Management")
        print("2. Member Management")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Issue/Return Records")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        try:

            if choice == "1":

                book_menu(library)

            elif choice == "2":

                member_menu(library)

            elif choice == "3":

                book_id = input(
                    "Enter Book ID: "
                ).strip()

                member_id = input(
                    "Enter Member ID: "
                ).strip()

                library.issue_book(
                    book_id,
                    member_id
                )

            elif choice == "4":

                book_id = input(
                    "Enter Book ID to return: "
                ).strip()

                library.return_book(book_id)

            elif choice == "5":

                library.view_transactions()

            elif choice == "6":

                print("\nThank you for using Library Management System!")

                break

            else:

                print("\nInvalid choice. Please enter 1-6.")

        except ValueError as error:

            print(f"\nError: {error}")

        except Exception as error:

            print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()