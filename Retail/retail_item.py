def get_retail_item_description():
    """
    Gets a return item from the console
    :return: The retail item description from user
    """
    description = input("Retail item description:")
    return description


def get_number_of_purchased_items():
    """
    Gets the number of purchased items from the console
    :return: The number of purchased items as an int
    """
    quantity = int(input("How many:"))
    return quantity


def get_price_per_unit():
    """
    Get the price from unit as a flat
    """
    price = float(input("How much:"))
    return price


def get_tax_rate():
    """
    Get tax rate from user as a float from 0.0 - 1.0
    """
    tax_rate = float(input("Tax rate:"))
    return tax_rate


def calculate_subtotal(price, quantity_sold):
    """
    Calculates the subtotal from the price and quantity
    """
    return price * quantity_sold


def calculate_tax(subtotal, tax_rate):
    """
    calculate the tax on the subtotal
    """
    tax_amount = subtotal * tax_rate
    return tax_amount


def calculate_total(subtotal, tax_amount):
    """
    calculates the total price from the subtotal and tax
    """
    total_price = subtotal + tax_amount
    return total_price


def main():
    """ Main Entry Point to Program"""
    description = get_retail_item_description()
    num_items = get_number_of_purchased_items()
    item_price = get_price_per_unit()
    tax_rate = get_tax_rate()

    subtotal = calculate_subtotal(item_price, num_items)
    tax = calculate_tax(subtotal, tax_rate)
    total = calculate_total(subtotal, tax)

    print("Sales receipt:")
    print("item Description:", description)
    print("Number of Purchased Items:", num_items)
    print("Unit Price:", item_price)
    print("Tax Rate:", tax_rate)
    print("Subtotal:", subtotal)
    print("Tax:", tax)
    print("Total:", total)


if __name__ == "__main__":
    main()


