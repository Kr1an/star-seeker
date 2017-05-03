"""Main Sequence Module.
    
    Module needed to calculate mass from star B-V value
    Function is not perfect(linealized and depend on interval)
    Calculates value depend on range: [0, 1] and (1, 2]
    
    Math functions that calculates luminosity: 
    -If point is in first range [0, 1] than 
        linearization will be: y=-40,14999*x + 31,1659090
    
    -If point lays within second range (1, 2] than
        linearization will be: y=-0.24087999*x + 0.4074183999
    
    
    Based on luminosity, calculates mass baised on:
        M = L ^ 0.3
    
    
    Module is not tested yet
    
"""


def _get_luminosity(value):
    """Function gets luminosity
    
    It is private function and other module function depends on it.
    If you need to get luminosity coefficient, you can you _get_luminosity
    
    Arguments:
        value: B-V value of specific star
    
    Returns:
        value: luminosity coefficient of specific star relative to
            Sun luminosity coefficient L/Lo
    
    """
    if 0 <= value < 0.5:
        return -40.14999*float(value) + 31.1659090
    elif 0.5 <= value <= 2:
        return -0.2408799*float(value) + 0.4074183999
    else:
        return None


def get_mass(value):
    """Function gets mass
    
    Function gets mass value from B-V of specific star.
    
    Arguments:
        value: B-V value of specific star
    
    Returns:
        value: mass of specific star relative to Sun mass( M/Mo )
    
    """
    luminosity = _get_luminosity(value)
    if luminosity <= 0:
        return None
    mass = luminosity ** 0.3;
    if mass <= 0:
        return None

    return luminosity ** 0.3;