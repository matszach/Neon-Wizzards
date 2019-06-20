from math import cos, sin, pi, sqrt, atan


def polar_to_cartesian(deg, radius):
    x = radius * sin(deg / 180 * pi)
    y = -radius * cos(deg / 180 * pi)
    return x, y


def cartesian_to_polar(x, y):

    # temp fix todo
    if x == 0:
        x = 0.0001

    deg = atan(y/x)/pi * 180 + 90
    if x < 0:
        deg += 180
    elif y < 0:
        deg += 360
    radius = sqrt(x**2 + y**2)
    return deg, radius
