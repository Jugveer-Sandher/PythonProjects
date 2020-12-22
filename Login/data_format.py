def get_book_info():
    """ Gets information about the book and returns a string"""
    book_title = input("Enter book title:")
    book_title_new = book_title.strip()

    book_isbn = int(input("Enter book ISNB:"))

    author_name = input("Enter authors last name:")
    author_name_new = author_name.strip()

    book_publisher = input("Who published the book:")
    book_publisher_new = book_publisher.strip()

    year_published = int(input("Enter year published:"))

    book_price = float(input("Enter book price:"))

    return "%s/%d/%s/%s/%d/%.2f" %(book_title_new, int(book_isbn), author_name_new, book_publisher_new,int(year_published), float(book_price))


def to_csv_format(book_info):
    """ Makes a CSV formatted version of get_book_info() """
    csv_string = book_info.replace("/", ",")
    return(csv_string)


def to_json_format(book_info):
    """ Makes a JSON formatted version of get_book_info() """
    index = book_info.find(",")
    title = book_info[0:index]
    book_info = book_info[index + 1:]

    index = book_info.find(",")
    isbn = book_info[0:index]
    book_info = book_info[index + 1:]

    index = book_info.find(",")
    author = book_info[0:index]
    book_info = book_info[index + 1:]

    index = book_info.find(",")
    publisher = book_info[0:index]
    book_info = book_info[index + 1:]

    index = book_info.find(",")
    year = book_info[0:index]
    book_info = book_info[index + 1:]

    index = book_info.find(",")
    price = book_info[0:index]
    book_info = book_info[index + 1:]

    json_string = "{\"title\":\"" + title + "\","\
                  + "\"ISBN\":\"" + isbn + "\"," \
                  + "\"Author last name\":\"" + author + "\"," \
                  + "\"Publisher\":\"" + publisher + "\"," \
                  + "\"Year\":\"" + year + "\"," \
                  + "\"Price\":\"" + price + "\"}"
    return json_string
