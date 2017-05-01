import sys, json, inspect, os
from utils.image_parser import *
import os

def get_parsed_arguments():
    photo_paths = json.loads(sys.stdin.readlines()[0])
    return photo_paths


def get_returned_object(photo_paths):
    return [
        {
          "header": 'statistic1',
          "content": 'Some statistic written here. Nothing special just some plain row text and nothing more. Hello world or hellow world i do not know.'
        },
        {
          "header": 'statistic2',
          "content": 'Some statistic written here. Nothing special just some plain row text and nothing more. Hello world or hellow world i do not know.'
        },
        {
          "header": 'statistic3',
          "content": 'Some statistic written here. Nothing special just some plain row text and nothing more. Hello world or hellow world i do not know.'
        }
    ]


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
