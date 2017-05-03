import math

def temperature_calculation(delta_m_color_index_array):
    min_temperature = 1e30
    max_temperature = 0
    total_temperarure = 0
    temperature_array = []
    for i in xrange(len(delta_m_color_index_array)):
        temperature_array.append(7920/(math.fabs(delta_m_color_index_array[i]) + 0.72))
    for i in xrange(len(temperature_array)):
        total_temperarure += temperature_array[i]
        if min_temperature > temperature_array[i]:
            min_temperature = temperature_array[i]
        if max_temperature < temperature_array[i]:
            max_temperature = temperature_array[i]
    average_temperature = total_temperarure / len(temperature_array)

    return (int(min_temperature), int(max_temperature), int(average_temperature))


def get_string_with_temperature(delta_m_color_index_array):

    temperature_array = temperature_calculation(delta_m_color_index_array)
    return {
        "header":"Temperature",
        "content":
        "Minimum star temperature in cluster: " + str(temperature_array[0]) + " celsius. "
        + "Maximum temperature: "+ str(temperature_array[1]) + " celsius. "
        +  "<T>: " + str(temperature_array[2])}