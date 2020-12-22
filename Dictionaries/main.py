import utilities_set
import utilities_dict


def main():
    """ Main Program """

    # PART A

    set1 = {'apple', 'banana', 'orange', 'peach'}
    set2 = {'banana', 'pineapple', 'peach', 'watermelon'}

    set1_count = utilities_set.get_total_items(set1)
    print("The total number of items in set1 is:", set1_count)
    print()

    print("Displaying the items of the set1:")
    utilities_set.display_all_items(set1)
    print()

    utilities_set.add_item("grape", set1)
    print("Added a grape, new set items are: ")
    utilities_set.display_all_items(set1)
    print()

    utilities_set.remove_item("orange", set1)
    print("Removed orange, new set items are: ")
    utilities_set.display_all_items(set1)
    print()

    set3 = utilities_set.get_the_union_of(set1, set2)
    print("The union of set1 and set2 is: ")
    utilities_set.display_all_items(set3)
    print()

    # # PART B

    provinces = {"alberta": "edmonton",
                 "ontario": "toronto",
                 "quebec": "quebec city",
                 "nova scotia": "halifax",
                 "new brunswick": "fredericton",
                 "manitoba": "winnipeg",
                 "prince edward island": "charlottetown",
                 "saskatchewan": "regina",
                 "newfoundland and labrador": "st. john's",
                 "yukon": "whitehorse",
                 "nunavut": "iqaluit",
                 "northwest territories": "yellowknife",
                 "british columbia": "victoria"}

    print("The current dictionary contains: ")
    utilities_dict.display_all(provinces)
    print()

    print("The capital for Yukon is:", utilities_dict.get_capital_city("yukon", provinces))
    print()

    print("removing Manitoba from list: ")
    utilities_dict.remove_province("manitoba", provinces)
    utilities_dict.display_all(provinces)
    print()

    print("Adding Manitoba back: ")
    utilities_dict.add_province("manitoba", "winnipeg", provinces, )
    utilities_dict.display_all(provinces)
    print()

    # PART C

    canada = {
        "alberta": {"capital": "edmonton", "largest": "calgary", "population": 3645257},
        "ontario": {"capital": "toronto", "largest": "toronto", "population": 12851821},
        "quebec": {"capital": "quebec city", "largest": "montreal", "population": 7903001},
        "nova scotia": {"capital": "halifax", "largest": "halifax", "population": 921727},
        "new brunswick": {"capital": "fredericton", "largest": "saint john", "population": 751171},
        "manitoba": {"capital": "winnipeg", "largest": "winnipeg", "population": 1208268},
        "prince edward island": {"capital": "charlottetown", "largest": "charlottetown", "population": 140204},
        "saskatchewan": {"capital": "regina", "largest": "saskatoon", "population": 1033381},
        "newfoundland and labrador": {"capital": "st. john's", "largest": "st. john's", "population": 514536},
        "yukon": {"capital": "whitehorse", "largest": "whitehorse", "population": 33897},
        "nunavut": {"capital": "iqaluit", "largest": "iqaluit", "population": 31906},
        "northwest territories": {"capital": "yellowknife", "largest": "yellowknife", "population": 41462},
        "british columbia": {"capital": "victoria", "largest": "vancouver", "population": 4400057}
    }

    print("The total population of the provinces are:", utilities_dict.get_total_population(canada))
    print()

    print("The smallest province is:", utilities_dict.get_smallest_province(canada))
    print()

    print("The largest province is:", utilities_dict.get_largest_province(canada))
    print()

    print("The capital of Yukon is:", utilities_dict.get_another_capital_city ("yukon", canada))
    print()

    print("The largest city of Quebec is:", utilities_dict.get_largest_city("quebec", canada))


if __name__ == '__main__':
    main()
