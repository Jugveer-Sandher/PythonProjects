import random

MONTHS_IN_YEARS = 12


def loan_qualifier():
    """ Check if person qualifies for loan."""
    month_salary = float(input("Enter monthly salary:"))
    years_emp = int(input("Enter how many years employed:"))

    annual_salary = month_salary * MONTHS_IN_YEARS

    if annual_salary >= 50000 and years_emp >= 3:
        print("You qualify for a loan.")
    if annual_salary < 50000:
        print("Your income must be 50000 or more, you don’t qualify for a loan.")
    if years_emp < 3:
        print("You must be employed for 3 years or more, you don't qualify for a loan.")


def is_magic_date():
    """Finds the magic date after entering values"""
    month_val = int(input("Enter month value:"))
    if month_val > 12 or month_val < 1:
        print("Invalid month value.")

    day_val = int(input("Enter day value:"))
    if day_val > 31 or day_val < 1:
        print("The day value must be between 1 and 31.")

    year_str = input("Enter year value:")
    year = int(year_str)
    if len(year_str) != 2 or year < 0 or year > 99:
        print("The year value must be positive and it must be two digit.")
        return

    if (day_val * month_val) == year:
        print(" the date", day_val, "-", month_val, "-", year, "is a magic date")
    else:
        print(" the date", day_val, "-", month_val, "-", year, "is not a magic date")


def play_chicago():
    """plays the multi-round game of Chicago """

    play_again = "yes"
    round_count = 2
    points = 0

    while round_count <= 12 and play_again == "yes":
        print("round number ", round_count)

        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        print("first dice number is", num1)
        print("second dice number is", num2)

        if num1 + num2 == round_count:
            points += 1
            print("you won a point")
        else:
            print("no points this round")

        print("your current points are", points)

        round_count += 1

        play_again = input("Do you want to play again?, enter \"yes\" to continue:")
        play_again.lower()
        play_again.strip()

    print("the game is over you earned", points, "points")


def is_even(number):
    """checks if the number entered is even or odd"""
    if number % 2 == 0:
        return True
    else:
        return False


def get_pocket_colour(number):
    """pick a number and the number is corresponded with a number"""

    if number == 0:
        return "green"
    elif number <= 10 and is_even(number) is True:
        return "black"
    elif number <= 10 and is_even(number) is False:
        return "red"
    elif number <= 18 and is_even(number) is True:
        return "red"
    elif number <= 18 and is_even(number) is False:
        return "black"
    elif number <= 28 and is_even(number) is True:
        return "black"
    elif number <= 28 and is_even(number) is False:
        return "red"
    elif number <= 36 and is_even(number) is True:
        return "red"
    elif number <= 36 and is_even(number) is True:
        return "black"


def play_roulette():
    """Playing the game roulette"""

    total = 0
    amount_bet = 0
    play_again = "yes"

    while play_again == "yes":
        number = int(input("Enter your pocket number:"))
        if number < 0 or number > 36:
            print("Number needs to be between 1-36, try again")
            number = int(input("Enter your pocket number:"))

        amount_bet = int(input("How much are you betting?"))

        if get_pocket_colour(number) == "green":
            print("you did not win or lose")
        elif get_pocket_colour(number) == "black" and is_even(number) is True:
            amount_bet *= 1.5
            total += amount_bet
            print("You won 50% for the:", amount_bet, "$")
        elif get_pocket_colour(number) == "red" and is_even(number) is True:
            amount_bet *= 2
            total += amount_bet
            print("You won 100% for the bet:", amount_bet, "$")
        elif get_pocket_colour(number) == "black" and is_even(number) is False:
            total -= amount_bet
            print("Sorry you lost, amount:", amount_bet, "$")
        elif get_pocket_colour(number) == "red" and is_even(number) is False:
            amount_bet *= 1.5
            total += amount_bet
            print("You won 50% from the bet:", amount_bet, "$")

        print("you have in total", total)
        play_again = input("Do you want to play again?, enter \"yes\" to continue:")
        play_again.lower()
        play_again.strip()

    print("Game over you have in total", total)


def main():
    """ lab 3 """
    loan_qualifier()
    is_magic_date()
    play_chicago()
    is_even(6)
    play_roulette()


if __name__ == "__main__":
    main()


