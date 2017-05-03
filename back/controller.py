import sys, json, inspect, os
from utils import image_parser
from utils import magnitude
from utils import color_index
from utils import special_value
from utils import main_sequence
from utils import age_module
from utils import pixel_module
from utils import temperature_module
import os


def get_parsed_arguments():
    photo_paths = json.loads(sys.stdin.readlines()[0])
    return photo_paths


def get_returned_object(photo_paths):
    statistics = []

    # return {'name': 'test'}
    yellow_stars_array = image_parser.image_parser(
        photo_paths['yellowFilterFilePath']
    )
    blue_stars_array = image_parser.image_parser(
        photo_paths['blueFilterFilePath']
    )
    # return blue_stars_array + [-1,-1,-1] + yellow_stars_array
    blue_magnitude_array = []
    yellow_magnitude_array = []
    yellow_magnitude_array, blue_magnitude_array = magnitude.pogson_calculation(
        yellow_stars_array, blue_stars_array
    )
    # return blue_magnitude_array

    delta_m_color_index_array = color_index.get_color_index_calculation(
        blue_magnitude_array,
        yellow_magnitude_array
    )

    # return yellow_stars_array
    # return delta_m_color_index_array
    # return {'argument': len(delta_m_color_index_array), 'value': len(yellow_magnitude_array)}

    s_value = special_value.get_special_value(
        delta_m_color_index_array,
        blue_magnitude_array
    )
    # return s_value
    # # return s_value
    # return {'value': s_value}

    # return {'name': s_value}
    special_star_mass = main_sequence.get_mass(s_value)+1.2
    # return {'name': special_star_mass}

    cluster_age = age_module.age_calculation(special_star_mass)
    # return {'name': cluster_age}

    # return delta_m_color_index_array
    statistics += [temperature_module.get_string_with_temperature(
        delta_m_color_index_array
    )]
    # return statistics[0]


    statistics += [pixel_module.get_pixel_statistics(blue_stars_array, yellow_stars_array)]

    statistics += [age_module.get_statistic(cluster_age)]
    # return delta_m_color_index_array

    return statistics


def is_photo_paths_valide(photo_paths):
    try:
        if os.path.exists(photo_paths['yellowFilterFilePath']):
            if os.path.exists(photo_paths['blueFilterFilePath']):
                return True
        return False
    except:
        return False


def main():
    photo_paths = get_parsed_arguments()
    if is_photo_paths_valide(photo_paths):
        returned_object = get_returned_object(photo_paths)
        print json.dumps(returned_object)
    else:
        print ''


if __name__ == '__main__':
    main()
