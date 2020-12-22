def generate_login(first, last, id):
    """ Genrates a login ID for a BCIT student """
    formatted_first = first.title()
    formatted_last = last.title()

    if len(formatted_first) > 3:
        first_part = formatted_first[0:3]
    else:
        first_part = formatted_first

    if len(formatted_last) > 3:
        second_part = formatted_last[0:3]
    else:
        second_part = formatted_last

    if len(id) > 3:
        third_part = id[-3:]
    else:
        third_part = id

    return "%s%s%s" % (first_part, second_part, third_part)


def has_upper(word):
    """ returns true if there is an upper case """
    index = 0
    while index < len(word):
        if word[index].isupper():
            return True
        index += 1
    return False


def has_lower(word):
    """ returns true if there is an upper case """
    index = 0
    while index < len(word):
        if word[index].islower():
            return True
        index += 1
    return False


def has_digit(word):
    """ returns true if there is an upper case """
    index = 0
    while index < len(word):
        if word[index].isdigit():
            return True
        index += 1
    return False


def change_password():
    """ Allows a password that is complex"""
    print("enter a password with at least 7 characters long with one uppercase, one lowercase and one number. It cannot"
          "have complex character")

    valid = False

    while not valid:
        password = input("enter password:")

        if len(password) > 7 and has_upper(password) and has_lower(password) and has_digit(password) and password.isalnum():
            valid = True
        else:
            if len(password):
                print("the length needs to be 7 or more")

            if not has_upper(password):
                print("must have at least one uppercase")

            if not has_lower(password):
                print("must have a lowercase")

            if not has_digit(password):
                print("must have a digit")

            if not password.isalnum():
                print("cannot have special characters")

    return password
