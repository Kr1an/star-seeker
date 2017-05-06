"""Maximum Bright Module

Module to get maximum bright star
"""

from image_parser import image parser

def get_brightness_of_bright_star(file_path):
    """Function calculate maximum bright star.
        Arguments:
            file_path: path to file with bright star
        Returns:
            value: bright of maximum brightness star
    """
    array_stars = []
    array_stars = image_parser(file_path)
    max_bright_star = 0
    for i in xrange(len(array_stars)):
        if max_bright_star < array_stars[i]:
            max_bright_star = array_stars[i]
    return max_bright_star
