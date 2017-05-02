"""Magnitude Module

Module allows to find magnitude of stars array. From pixels 
that where lighted by specific star.

Use pogson_calculation function to make calculations.
It uses formula from Pogson formula: log10(E1/E2)/0.4

And calculate magnitude for every star in two arrays - blue filter
array and yellow filter array.

"""
import math


def _pogson_calculation_specific(E1, stars):
    """Calculate magnityte coefficient for array values
    
    Do not use function outside of this module. Use Pogson_calculation
    instead.
    
    Function calculates relative magnitude of array of values.
    
    Arguments:
        E1: magnitude of relative star
        stars: array of stars, which relative magnitude should
            be calculated.
    
    Returns:
        value: array of magnitude initial star array.
    
    
    """
    array_magnitude = []
    for i in xrange(len(stars)):
        delta_m = math.log10(float(E1) / stars[i]) / 0.4
        array_magnitude.append(delta_m)
    return array_magnitude


def pogson_calculation(yellow, blue):
    """Function calculated magnitude
    
    This function is a main module function. Use it to find magnitude
    array from two area arrays: yello, blue
    
    Arguments:
        yellow: array of stars area in yellow filter.
        blue: array of stars areas in blue filter.
    
    Returns:
        value: two arrays of magnitude values for both filters
    
    """
    E1 = yellow[0]
    array_delta_m_blue = _pogson_calculation_specific(E1, blue)
    array_delta_m_yellow = _pogson_calculation_specific(E1, yellow)
    return [array_delta_m_yellow, array_delta_m_blue]