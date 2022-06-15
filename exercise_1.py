from math import sqrt


def calculate_area_and_perimeter(base: float, height: float):
    area = (base * height) / 2
    perimeter = base + height + calculate_hypotenuse(base, height)

    return area, perimeter


def calculate_hypotenuse(base: float, height: float) -> float:
    hypotenuse = base ** 2 + height ** 2
    return round(sqrt(hypotenuse), 1)
