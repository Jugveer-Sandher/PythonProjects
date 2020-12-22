import sys
import login
import data_format


def main():
    """ Main program """
    if len(sys.argv) != 4:
        print("Invalid Arguments")
        exit(0)

    login_id = login.generate_login(sys.argv[1],
                             sys.argv[2],
                             sys.argv[3])

    print("login id is %s" % login_id)

    new_password = login.change_password()
    print("New password is %s" % new_password)


if __name__ == '__main__':
    # main()
    book_info = data_format.get_book_info()
    csv_format = data_format.to_csv_format(book_info)
    json_string = data_format.to_json_format(csv_format)
    print("CSV Formatted String:")
    print(csv_format)
    print("JSON Formatted String:")
    print(json_string)
