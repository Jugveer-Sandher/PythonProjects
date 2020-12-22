def get_total_items(set1):
    """ Returns the total number of items for the give set1 """
    if isinstance(set1, set):
        return len(set1)
    return 0


def display_all_items(set1):
    """ Prints all the given elements for set1 """
    if isinstance(set1, set):
        for item in set1:
            print(item)


def add_item(item, set1):
    """ Adds the give item to the set """
    if isinstance(set1, set):
        set1.add(item)


def remove_item(item, set1):
    """ Removes the given item from the set """
    if isinstance(set1, set):
        set1.discard(item)


def get_the_union_of(set1, set2):
    """ Returns a set of the union given in the parameters """
    if isinstance(set1, set) and isinstance(set2, set):
        return set1.union(set2)
