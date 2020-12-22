def weight_converter():
    """ converts kilos into pounds and displays it on a table """

    for kilos in range(30, 101, 10):
        print("  weight in Kilos: %4d is %6.2f in Pounds" % (kilos, kilos * 2.2))


def get_divisible():
    """ find all numbers divisible eby a given number within a range """
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    divisor = int(input("Enter divisor: "))

    if divisor == 0:
        print("The divisor cannot be 0")
    elif num1 < num2:

        for num in range(num1, num2 + 1):
            if (num % divisor) == 0:
                print(num, end=" ")

    else:

        for num in range(num1, num2 + 1, -1):
            if (num % divisor) == 0:
                print(num, end=" ")

    print()


def get_list_stats():
    """ display stats on a user entered list of integers """

    user_input = ""
    user_list = []

    while user_input != " ":
        user_input = input("Enter an integer: ")

        if user_input.isnumeric():
            user_list.append(int(user_input))
        else:
            print("Not an integer. Ignoring.")

    print(user_list)
    print(len(user_list))

    num_even = 0
    min_val = user_list[0]
    max_val = user_list[0]

    for num in user_list:
        if num % 2 == 0:
            num_even += 1

        if num < min_val:
            min_val = num

        if num > max_val:
            max_val = num

    sorted_list = sorted(user_list)
    min_val = sorted_list[0]
    max_val = sorted_list[-1]

    print("Num Evens: %d" % num_even)
    print("Min: %d" % min_val)
    print("Mac: %d" % max_val)


def calculate_pay(number_of_employees, hourly_rate):
    """ calculates the pay of how many hours the worker worked and put it into a list """

    employee_list = []

    while number_of_employees > len(employee_list):
        worked_hours = int(input("input the number of worked hours: "))

        pay = 0
        pay += (worked_hours * hourly_rate)

        if worked_hours > 40:
            overtime = (worked_hours - 40)
            pay -= (overtime * hourly_rate)
            pay += (overtime * (hourly_rate * 1.5))

        inner_list = [worked_hours, pay]
        employee_list.append(inner_list)

    index = 0

    while index < len(employee_list):
        print("the employee worked for %d hours and earned %.2f $" % (employee_list[index][0], employee_list[index][1]))
        index += 1


def is_prime(nums):
    """ Checks if a the number is prime, if it is it returns true otherwise false"""

    if nums < 0:
        print("Number must be greater than 0")

    if nums == 2:
        return True

    for i in range(2, nums):
        if (nums % i) == 0:
            return False

    return True


def get_prime_numbers(prime_number):
    """ Checks if numbers in a list greater than two are prime numbers """

    for i in range(2, prime_number + 1):
        if is_prime(i):
            print("the number %d is a prime number" % i)


def main():
    """ Main Program """

    weight_converter()

    # get_divisible()

    # get_list_stats()

    # number_of_employees = int(input("Enter number of employees: "))
    # hourly_rate = float(input("Enter hourly rate: "))
    # calculate_pay(number_of_employees, hourly_rate)

    # is_prime(nums)

    # prime_number = int(input("Enter a number, which is larger than 2: "))
    # if prime_number < 2:
    #     print("Number needs to be larger than 2")
    # get_prime_numbers(prime_number)


if __name__ == '__main__':
    main()
