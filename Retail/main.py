import utilities


def main():
    radius1 = int(input("Enter the radius of the circle in cm:"))
    print(" The area of the circle:", utilities.calculate_circle_area(radius1))
    radius2 = int(input("Enter the radius of the sphere in cm:"))
    print(" The volume of the sphere:", utilities.calculate_sphere_volume(radius2))
    weight = float(input("Enter your weight in kilograms:"))
    height = float(input("Enter your height meters:"))
    print(" The Body Mass Index is:", utilities.calculate_bmi(weight, height))
    side_a = float(input("Enter the side A in cm:"))
    side_b = float(input("Enter the side B in cm:"))
    print(" The hypotenuse of the the right triangle is:", utilities.calculate_hypotenuse(side_a, side_b))


if __name__ == "__main__":
    main()
