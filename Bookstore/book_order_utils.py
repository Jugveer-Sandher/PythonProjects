import re
import os.path


def validate_book_order_details(order_num, title, author, isbn, year, quantity, cost):
    """ Validates a book order """

    if re.search(r"^\d+$", order_num) is None:
        raise ValueError("Order Number is invalid")

    if re.search(r"^[a-zA-Z ]+$", title) is None:
        raise ValueError("Title is invalid")

    if re.search(r"^[a-zA-Z ']*$", author) is None:
        raise ValueError("Author is invalid")

    if re.search(r"^\d*$", isbn) is None:
        raise TypeError("ISBN must be an integer")
    if len(isbn) < 4 or len(isbn) > 20:
        raise ValueError("ISBN is invalid")

    if re.search(r"^\d*$", year) is None:
        raise TypeError("Year must be an integer")
    if len(year) != 4:
        raise ValueError("Year is invalid")

    if re.search(r"^\d*$", quantity) is None:
        raise TypeError("Quantity must be an integer")
    if int(quantity) < 0 or int(quantity) > 1000:
        raise ValueError("Quantity is invalid")

    if re.search(r"^\d*.\d{2}$", cost) is None:
        raise ValueError("Cost is invalid")


def calculate_per_book_cost(cost, quantity):
    """ Returns a floating point value that is the cost per book """

    return float(cost) / int(quantity)


def write_book_order_details(filename, title, author, isbn, year, quantity, cost, unit_cost):
    """ Creates a file with the given filename which holds the details """

    if os.path.isfile(filename):
        raise ValueError("Order file name already exists!")

    fh = open(filename, "w")
    fh.write("BOOK ORDER\n")
    fh.write("tile=%s\n" % title)
    fh.write("author=%s\n" % author)
    fh.write("isbn=%s\n" % isbn)
    fh.write("year=%s\n" % year)
    fh.write("quantity=%s\n" % quantity)
    fh.write("cost=$%s\n" % cost)
    fh.write("unit_cost=$%s\n" % unit_cost)
    fh.close()
