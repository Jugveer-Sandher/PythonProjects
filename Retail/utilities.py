import math


def calculate_circle_area(radius):
    """
    Gets the radius as a parameter squares it and multiplies it by pi
    :return: The circle's area.
    """
    area = math.pi * radius ** 2
    return area


def calculate_sphere_volume(radius):
    """
    Gets the volume of the circle through getting the radius as a parameter
    :return: Circle's volume
    """
    volume = 4/3 * math.pi * radius ** 3
    return volume


def calculate_bmi(weight, height):
    """
    Calculates the body mass index (BMI) by getting the weight in kg and height in meters as a parameter
    :return: The BMI
    """
    bmi = float(weight / (height * height))
    return bmi


def calculate_hypotenuse(side_a, side_b):
    side_c = float(math.hypot(side_a, side_b))
    return side_c
