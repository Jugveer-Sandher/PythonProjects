class Car:
    """ Represents a car lot """

    def __init__(self, make, model, year, cost, price):
        """ Initilizes the car details """
        self._make = make
        self._model = model
        self._year = year
        self._cost = cost
        self._price = price

    def calc_profit(self):
        """ Returns projected profit """
        return self._price - self._cost

    def get_details(self):
        """ Returns a formatted string of the car details """
        return "%d %s %s for sale for $%.2f" % (self._year, self._make, self._model, self._price)

    def reduce_price(self, reduction):
        """ Returns a reduced price of the car """
        self._price = self._price - reduction
