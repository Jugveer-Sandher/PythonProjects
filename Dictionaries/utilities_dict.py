# PART B


def display_all(this_dict):
    """ Displays the key/values pairs in the dictionary """
    if isinstance(this_dict, dict):
        for key, value in this_dict.items():
            print("%s is the capital city of %s" % (value, key))


def get_capital_city(province_name, this_dict):
    """ Returns the capital of the given province """
    if isinstance(this_dict, dict):
        return this_dict.get(province_name, "Province not found")


def add_province(province_name, capital_city, this_dict):
    """ Adds a province and capital city """
    if isinstance(this_dict, dict):
        this_dict[province_name] = capital_city


def remove_province(province_name, this_dict):
    """ Removes a province from the dict """
    if isinstance(this_dict, dict):
        if province_name in this_dict:
            del this_dict[province_name]


# PART C


def get_total_population(this_dict):
    """ Gets the total population """
    population = 0
    if isinstance(this_dict, dict):
        for x in this_dict:
            population += this_dict[x]["population"]

        return population


def get_another_capital_city(province_name, this_dict):
    """ returns the capital city of the province entered """
    if isinstance(this_dict, dict):
        for x in this_dict:
            if x == province_name:
                return this_dict[province_name]["capital"]
        return " "


def get_largest_city(province_name, this_dict):
    """ Returns the largest city of the province that is entered """
    if isinstance(this_dict, dict):
        for x in this_dict:
            if x == province_name:
                return this_dict[province_name]["largest"]
        return " "


def get_largest_province(this_dict):
    """ Returns the province with the most population """
    if isinstance(this_dict, dict):
        largest = 0
        for x in this_dict:
            if this_dict[x]["population"] > largest:
                largest = this_dict[x]["population"]
                province = x

        return province


def get_smallest_province(this_dict):
    """ Returns the province with the least population """
    if isinstance(this_dict, dict):
        smallest = 100000000
        for x in this_dict:
            if this_dict[x]["population"] < smallest:
                smallest = this_dict[x]["population"]
                province = x

        return province
