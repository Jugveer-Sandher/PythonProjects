import re


def is_valid_bc_license_plate(plate):
    """ Check for a valid BC license plate and comes true if it is valid """
    patter1 = "^[A-Z]{3}\d{3}$"
    pattern2 = "^\d{3}[A-Z]{3}$"
    pattern3 = "^[A-Z]{2}\d[ -]\d{2}[A-Z]$"
    regex = "%s|%s|%s" % (patter1, pattern2, pattern3)

    if re.search(regex, plate):
        return True
    return False


def is_valid_python_variable_name(variable):
    """ Checks for a valid python variable name and returns true if so """

    if re.search("^[a-z_]{1,32}$", variable):
        if re.search("[a-z]+__[a-z]+", variable) is None:
            return True
    return False


def is_valid_email_adress(email):
    """ Checks for a valid email address and returns true if so """

    email_data = re.split('@', email)
    username = email_data[0]
    domain_data = re.split('[.]', email_data[1])
    domain_name = domain_data[0]
    top_level_domain = domain_data[1]

    if re.search("^[a-zA-Z]+_*[a-zA-Z]{1,256}$", username):
        if re.search("^[a-zA-Z]{1,32}$", domain_name):
            if re.search("^[a-zA-Z]{2,5}$", top_level_domain):
                return True
    return False


def is_valid_human_height(height):
    """ Checks if human height is valid and returns true if so """

    pattern1 = '^[2-8]\'0?[1-9]("|in)$'
    pattern2 = '^[2-8]\'(10|11)("|in)$'

    if re.search(pattern1, height) or re.search(pattern2, height):
        return True
    return False


def main():
    """ Main Program"""
    license_ex = {"ABC123": True, "709XYZ": True, "AB1-23C": True, "AB1--23C": False,
                  "AB123C": False}

    is_license_function_good = True
    for plates, is_valid in license_ex.items():
        results = is_valid_bc_license_plate(plates)
        if results != is_valid:
            print("%s should be %s" % (plates, str(is_valid)))
            is_license_function_good = False

    if is_license_function_good:
        print("License plate validator is all good")

    print()

    variable_sample = {"the_dog": True, "the__dog": False, "abcdefghijklmnopqrstuvwxyzabcdef": True,
                       "abcdefghijklmnopqrstuvwxyzabcdefg": False,
                       "the_dog_is_spotted": True, "__main__": True}

    is_variable_function_good = True
    for variable, is_valid in variable_sample.items():
        results = is_valid_python_variable_name(variable)
        if results != is_valid:
            print("%s should be %s" % (variable, str(is_valid)))
            is_variable_function_good = False

    if is_variable_function_good:
        print("Python var validator all good")

    print()

    email_sample = {"8PqBpzyiU2pfzYXSDLdWwo7uh36U1GLOcvckAECAii2yYvd5tAMDGCDroPyXzP6TXTvcWQVXTGDhEWXouGRjg9VwP9g36uheOWZKG5HXKMLffwsadpy0GdCeHpb6dxEgoJQupH1oaAXIvX1lySjJ5Fw5pVYb9B8VYUcgJvvZZV9naX7r9VsGplbTHfkldIczgReGD6OSiZAHe3bIaCBHFlO2fRWG3QycWAUNOYJjmAmkvOAA1Og0gx0of8KkvgRD@bcit.cpm": False,
                    "jug_sandher@abcdefghijklmnopqrstuvwxyzabcdfgh.ca": False, "_jug_sandher_@bcit.com": False,
                    "jug_sandher@bcit.comcom": False, "jug___sandher@bcit.ca": True, "jug_sandher@bcit.com": True
                    }

    is_email_function_good = True
    for email, is_valid in email_sample.items():
        results = is_valid_email_adress(email)
        if results != is_valid:
            print("%s should be %s" % (email, str(is_valid)))
            is_email_function_good = False

    if is_email_function_good:
        print("Email validator all good")

    print()

    height_sample = {"2'0\"": False, "9'0\"": False, "5'08\"": True, "8'11\"": True, "6'12\"": False, "3'10in": True,
                     "9'0in": False}

    is_height_function_good = True
    for height, is_valid in height_sample.items():
        results = is_valid_human_height(height)
        if results != is_valid:
            print("%s should be %s" % (height, str(is_valid)))
            is_height_function_good = False

    if is_height_function_good:
        print("Height validator all good")


if __name__ == '__main__':
    main()
