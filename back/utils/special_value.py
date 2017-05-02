"""Special Value Module


"""
from scipy import stats
import numpy as np
import math


def get_special_value(function_arguments=[], function_values=[]):
    """Function calculates special function argument
    
    Function allow you to find special function argument that
    needed to show point where stars leave main star sequence.
    Then this value's used for calculation star clauster age.
    
    Arguments:
        function_arguments: list of function arguments
        function_values: function values list
    
    Returns:
        value: argument that is equal to special value.
    
    """
    max_propogation = 0
    max_propogation_idx = 0
    slope, intercept, r_value, p_value, std_err = stats.linregress(function_arguments, function_values)
    angle = math.atan(slope)*180/math.pi
    if angle < 0:
        angle = 180 + angle
    angle_sin = math.sin(angle/float(180)*math.pi)

    for idx in range(len(function_arguments)):
        intersection_x = (function_values[idx] - intercept) / slope
        delta = function_arguments[idx] - intersection_x
        if delta < 0:
            continue
        propogation = angle_sin*delta
        if propogation > max_propogation:
            max_propogation = propogation
            max_propogation_idx = idx

    if angle > 90:
        angle = 180 - angle
    

    print(function_arguments[max_propogation_idx])
    return function_arguments[max_propogation_idx]

get_special_value([3,3,3,3,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,7,7,7,8], [3,4,5,6,3,4,5,6,2,3,4,5,6,7,1,2,3,4,8,1,2,8,8])