""" Calculation Distance To Star Module

Module allows to find distance to star.

Use pogson_calculation function to make calculations.
It uses formula from Pogson formula: log10(L1/L2)/0.4, where L1 -
luminosity of Sun.

And use formula to calculate distance to star: M = m + 5 - 5 * log10(r)

"""

import math

def get_distance_to_star(L, m):
    """Function calculate distance to star.

    Arguments:
        L: luminosity of star
        m: Apparent magnitude

    Returns:
        value: distance to star
    """
    M_Sun = 4.83
    M = M_Sun - math.log10(L)/0.4
    r = 10 ** ((m + 5 - M) / 5)
    return r
