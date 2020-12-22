import re
import json


def add_book():
    """ Adds a book into bookstore.json """
    title = input("Book title:")
    if re.search(r"^[a-zA-Z \d]+$", title) is None:
        raise ValueError("Title is invalid")

    author = input("Author name:")
    if re.search(r"^[a-zA-Z ]+$", author) is None:
        raise ValueError("Invalid author name")

    isbn = input("ISBN number:")
    if re.search(r"^\d{4,20}$", isbn) is None:
        raise ValueError("Invalid ISBN")

    year = input("Year published:")
    if re.search(r"^\d+$", year) is None:
        raise TypeError("Year must be an integer")
    int(year)
    if len(year) != 4 or year < '1900':
        raise ValueError("Invalid year")

    desc = input("Description:")
    if re.search(r".{0,256}", desc) is None:
        raise ValueError("Invalid description")
    if re.search(r".{0,256}", desc):
        desc = desc[:30]

    return title, author, year, isbn, desc


def save_book(book_list, filename):
    """ Saves the car list into a json file """
    book_file = open(filename, "w")
    book_json = json.dumps(book_list, indent=4)
    book_file.write(book_json)
    book_file.close()


def delete_book(book_list):
    """ Deletes a book from the database """
    user_isbn = (input("Enter ISBN number of the book:"))

    if re.search(r"^\d{4,20}$", user_isbn) is None:
        raise ValueError("Book not found, invalid isbn")
    for i in range(len(book_list)):
        if book_list[i]['isbn'] == user_isbn:
            del book_list[i]
            print("Book has been deleted")
            break


def get_description(book_list):
    """ Gets the description and prints it """
    for book in book_list:
        print("Title: %s, Author: %s,  Year: %s, ISBN: %s, Desc: %s" % (book["title"], book["author"], book["year"],
                                                                        book["isbn"], book["description"]))


def search_by_title(book_list):
    """ User enters title and program searches the database for the book with that title """
    user_title = input("Enter book title:")
    if re.search(r"^[a-zA-Z \d]+$", user_title) is None:
        raise ValueError("Title is invalid")

    match = False
    for x in book_list:
        if user_title.lower() in x["title"].lower():
            print("Title: %s, Author: %s,  Year: %s, ISBN: %s, Desc: %s" % (x["title"], x["author"], x["isbn"],
                                                                            x["year"], x["description"]))
            match = True
        if not match:
            print("No matches found")


def search_by_author(book_list):
    """ User enters author and program search the database for the information """
    user_author = input("Enter author name:")
    if re.search(r"^[a-zA-Z ']+$", user_author) is None:
        raise ValueError("Invalid author entered")

    match = False
    for x in book_list:
        if user_author.lower() in x["author"].lower():
            print("Title: %s, Author: %s,  Year: %s, ISBN: %s, Desc: %s" % (x["title"], x["author"], x["isbn"],
                                                                            x["year"], x["description"]))
            match = True
    if not match:
        print("No matches found")


def search_by_keyword(book_list):
    """ User enters keyword and program searches for the information that follows the keyword """
    user_keyword = input("Enter keyword:")
    if re.search(r"^.{1,20}$", user_keyword) is None:
        raise ValueError("Invalid keyword")

    match = False
    for x in book_list:
        if user_keyword.lower() in x["description"].lower():
            print("Title: %s, Author: %s,  Year: %s, ISBN: %s, Desc: %s" % (x["title"], x["author"], x["isbn"], x["year"], x["description"]))
            match = True
        elif user_keyword.lower() in x["title"].lower():
            print("Title: %s, Author: %s,  Year: %s, ISBN: %s, Desc: %s" % (x["title"], x["author"], x["isbn"], x["year"], x["description"]))
            match = True
    if not match:
        print("No matches were found")