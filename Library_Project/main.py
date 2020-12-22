import sys
import json
import os
import bookstore_util

book_list = []


def main():
    """ Main Program """

    # Add command line parameter
    filename = sys.argv[1]
    if len(sys.argv) != 2:
        print("Invalid parameters")

    user = " "

    if filename != "bookstore.json":
        print("The bookstore database does not exist")

    if os.path.isfile(filename):
        book_file = open(filename)
        data = book_file.read()
        book_file.close()
        if data != "":
            global book_list
            book_list = json.loads(data)
        else:
            book_list =[]

    while user != "q":

        try:
            user = input("Choose an action: Add book(a), Delete book(d), View book Summary(s), Search book by title(t),"
                         " Search book by author(u), Search book by keyword(k), Quit(q)")

            if user == "a":
                title, author, year, isbn, desc = bookstore_util.add_book()
                book = {"title": title, "author": author, "year": year, "isbn": isbn, "description": desc}
                for i in book_list:
                    print(i)
                    if i["isbn"] == isbn:
                        raise ValueError("Already same book with that isbn")
                book_list.append(book)
                bookstore_util.save_book(book_list, filename)

            elif user == "d":
                bookstore_util.delete_book(book_list)
                bookstore_util.save_book(book_list, filename)

            elif user == "s":
                bookstore_util.get_description(book_list)

            elif user == "t":
                bookstore_util.search_by_title(book_list)

            elif user == "u":
                bookstore_util.search_by_author(book_list)

            elif user == "k":
                bookstore_util.search_by_keyword(book_list)

            elif user == "q":
                print("Quitting Program")
                break

            else:
                raise ValueError("Invalid action input")

        except ValueError as v:
            print(v)
        except TypeError as t:
            print(t)


if __name__ == '__main__':
    main()

