"""Color Index Calculation Module

Module allows calculate color indexes
of arras blue and yellow filters stars.

"""


def get_color_index_calculation(delta_m_blue_array, delta_m_yellow_array):
    """Function calculate color indexes of arras blue and yellow filters stars.
    
    Arguments:
        delta_m_blue_array: array contains delta m with blue filter
        delta_m_yellow_array: array contains delta m with yellow filter
    
    Returns:
        value: array  contains color indexes delta m
    
    """
    delta_m_color_index_array = []
    for i in xrange(len(delta_m_yellow_array)):
        delta_m_color_index_array.append(delta_m_blue_array[i] - delta_m_yellow_array[i])
    return delta_m_color_index_array