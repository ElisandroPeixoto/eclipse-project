from cmath import rect, polar
from math import degrees, radians


def zero_sequence_component(ua: tuple, ub: tuple, uc: tuple) -> tuple:

    # Change angles to radians
    ua_radians = (ua[0], radians(ua[1]))
    ub_radians = (ub[0], radians(ub[1]))
    uc_radians = (uc[0], radians(uc[1]))

    # Calculate the zero sequence component
    u0 = polar((rect(*ua_radians) + rect(*ub_radians) + rect(*uc_radians)) / 3)

    # Round real part if the number is too small
    if u0[0] < 0.0001:
        u0_real = 0.000
    else:
        u0_real = u0[0]

    # Return the Zero Sequence Component, using three decimal places
    u0_degrees = (round(u0_real, 3), round(degrees(u0[1]), 3))

    return u0_degrees
