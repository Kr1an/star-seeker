"""Age Calculation Module
Module allows calculate
age of star cluster.
"""

def age_calculation(M):
    """Function calculate age
     of star cluster.
    Arguments:
        M: mass of star
    Returns:
        value: age of star cluster
    """
    return 10**10/M**3

def get_statistic(age):
    return {
        'header': 'Age',
        'content': 'Baised on pixel statistic, age of the star claster:' + age}