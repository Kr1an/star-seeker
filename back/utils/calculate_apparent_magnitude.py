"""Calculate Apparent Magnitude Module

Module allows to calculate apparent magnitude.

"""

import math

def get_apparent_margitude(E_wanted_star, E_bright_star, m_bright_star):
"""Function calculate apparent
    magnitude of wanted star
    Arguments:
        E_wanted_star: brightness of wanted star
        E_bright_star: brightness of bright star
        m_bright_star: apparent magnitude of bright star
    Returns:
        value: apparent magnitude of wanted star
"""
    m_wanted_star = m_bright_star - math.log10(E_wanted_star / E_bright_star)/ 0.4
    return m_wanted_star
