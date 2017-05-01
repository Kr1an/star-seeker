from PIL import Image
import numpy
import json
import os


VISITED = -999


def image_parser(file_path):
    """Image Parser

    Function that calculate number of specific objects on the photo. For
    example the number of start in the photo.

    Parameters:
        file_path: path with image, which we want to calculate.

    Returns:
        value: list of objects areas.

    """
    matrix = _get_gray_scale_bitmap_from_image(file_path)
    coefficient = _get_illumination_coefficient(matrix)

    stars = _get_objects_from_matrix_with_coefficient(matrix, coefficient)

    return stars


def _get_gray_scale_bitmap_from_image(file_path):
    """ Get Bitmap From Image

    Function that allow user to get gray scale image bitmap from particular
    file path.

    Parameters:
        file_path: string, that represents absolute path to file with image.

    Returns:
        value: matrix of values in range of [1..255] that represent element
            gray scale value in specific pixel.

    """
    image = Image.open(file_path)
    matrix = numpy.asarray(image.convert("L"))

    return matrix.tolist()


def _get_illumination_coefficient(matrix):
    """Get Illumination Coefficient

    Function that normalize matrix with values that describe objects.

    Returns:
        value: coefficient.

    """
    return _calculate_coefficient(matrix)


def _calculate_coefficient(matrix):
    return 35


def _get_objects_from_matrix_with_coefficient(matrix, coefficient):
    """ Get Objects From Matrix With Coefficient

    Function calculate showed off objects in the <matrix> by watching every
    elements and compare it's value to <coefficient>(if the element value is
    greater of equal then <coefficient>) grouping elements to
    one object if they are neighborhoods.

    Parameters:
        matrix: Matrix of values, by which we can alias element to
            specific group.
        coefficient: Value, that shows if the element is a part of
            needed object.

    Returns:
        value: list of values that describe area of each object.

    Example:
        call of _get_objects_from_matrix_with_coefficient with next
        params:
            matrix: [
                [0,0,5,5,0,0,0,0],
                [0,0,5,5,0,0,0,0],
                [2,0,0,0,0,0,0,0],
                [0,0,1,5,5,5,0,0],
                [0,0,0,5,5,0,0,0],
                [0,2,0,0,1,0,0,0],
                [0,5,0,0,0,2,5,5]
            ],
            coefficient: 3
        function returns next value:
            [4, 5, 1, 2] - this list describes every object in the matrix.

    """
    objects_area = []
    for row in xrange(len(matrix)):
        for col in xrange(len(matrix[row])):
            element_value = matrix[row][col]
            if element_value is VISITED or element_value < coefficient:
                matrix[row][col] = VISITED
                continue
            if element_value >= coefficient:

                elements_queue = []
                object_area = 0
                elements_queue.append({'i': row, 'j': col, 'value': element_value})
                matrix[row][col] = VISITED

                while len(elements_queue) is not 0:
                    cur = elements_queue.pop(0)
                    is_top = _is_inside_matrix(cur['i']-1, cur['j'], matrix)
                    is_right = _is_inside_matrix(cur['i'], cur['j']+1, matrix)
                    is_bottom = _is_inside_matrix(cur['i']+1, cur['j'], matrix)
                    is_left = _is_inside_matrix(cur['i'], cur['j']-1, matrix)
                    object_area += 1

                    if is_top and matrix[cur['i']-1][cur['j']] >= coefficient:
                        elements_queue.append({'i': cur['i']-1, 'j': cur['j'], 'value': matrix[cur['i']-1][cur['j']]})
                        matrix[cur['i'] - 1][cur['j']] = VISITED

                    if is_right and matrix[cur['i']][cur['j']+1] >= coefficient:
                        elements_queue.append({'i': cur['i'], 'j': cur['j']+1, 'value': matrix[cur['i']][cur['j']+1]})
                        matrix[cur['i']][cur['j'] + 1] = VISITED

                    if is_bottom and matrix[cur['i']+1][cur['j']] >= coefficient:
                        elements_queue.append({'i': cur['i']+1, 'j': cur['j'], 'value': matrix[cur['i']+1][cur['j']]})
                        matrix[cur['i'] + 1][cur['j']] = VISITED

                    if is_left and matrix[cur['i']][cur['j']-1] >= coefficient:
                        elements_queue.append({'i': cur['i'], 'j': cur['j']-1, 'value': matrix[cur['i']][cur['j']-1]})
                        matrix[cur['i']][cur['j'] - 1] = VISITED

                objects_area.append(object_area)

    return objects_area


def _is_inside_matrix(i, j, matrix):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])