from math import sqrt, atan, pi, sin, cos


def rect_to_polar(x: float, y:float) -> tuple:
    """Converts a rectangular coordinate (x,y) to polar coordinate (r,theta)"""
    r = sqrt(x**2 + y**2)
    theta_rad = atan(y/x)
    theta = theta_rad*(180/pi)

    return r, theta


def polar_to_rect(r: float, theta: float) -> tuple:
    """Converts a polar coordinate (r,theta) to rectangular coordinate (x,y)"""
    x = r*cos(theta*pi/180)
    y = r*sin(theta*pi/180)

    return x, y
