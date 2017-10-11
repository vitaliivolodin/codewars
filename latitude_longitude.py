# https://www.codewars.com/kata/coordinates-validator/train/python
import re


def is_valid_coordinates(coordinates):
    if re.match(r'^[-+]?([0-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$', coordinates):
        return True

    return False


if __name__ == '__main__':
    print(is_valid_coordinates("-23, 25"))