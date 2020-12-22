import sys
import book_order_utils


def main():
    """ Main Program """

    order_num = sys.argv[1]
    title = sys.argv[2]
    author = sys.argv[3]
    isbn = sys.argv[4]
    year = sys.argv[5]
    quantity = sys.argv[6]
    cost = sys.argv[7]

    if len(sys.argv) != 8:
        print("Invalid parameters")

    try:
        book_order_utils.validate_book_order_details(order_num, title, author, isbn, year, quantity, cost)
        book_order_utils.calculate_per_book_cost(cost, quantity)
        book_order_utils.write_book_order_details("0001.txt", title, author, isbn, year, quantity, cost,
                                                  book_order_utils.calculate_per_book_cost(cost, quantity))
    except TypeError as t:
        print("Type Error: %s" % t)
    except ValueError as v:
        print("Value Error: %s" % v)
    except ZeroDivisionError:
        print("No Books in Order")


if __name__ == '__main__':
    main()
