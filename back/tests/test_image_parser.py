"""Image Parser Unit Test Case.

This module is a test case for module utils.image_parser.
It tests functionality of:
    * def
    * def
    * def
    * def
    * def

Example:
    write 'python setup.py -t' in terminal.

Attributes:
    TEST_IMAGES_FOLDER_PATH: folder path with images for image_parser test
        case in it.

Test Module isn't finished.
Find particular test class or test in is's name(title).

"""

import unittest

import os
from utils import image_parser

TEST_IMAGES_FOLDER_PATH = \
    os.path.abspath(
        os.path.join(
            __file__,
            '..',
            'mock',
            'images_for_image_parser'
        )
    )


class PropertyReaderTestCase(unittest.TestCase):
    def setUp(self):
        self.folder_path = TEST_IMAGES_FOLDER_PATH
        self.img_paths = []
        for idx in xrange(4):
            self.img_paths.append(
                os.path.join(
                    self.folder_path,
                    'with_%d_stars.jpg' % idx
                )
            )

    def test_image_parser_is_number_of_stars_correct(self):
        for idx in xrange(4):
            self.assertEqual(
                len(image_parser.image_parser(self.img_paths[idx])),
                idx,
                "expected: %d, real: %d. Asserting error while"
                " numbers tests: len of result"
                " is not correct." % (
                    idx,
                    len(image_parser.image_parser(self.img_paths[idx]))
                )
            )
