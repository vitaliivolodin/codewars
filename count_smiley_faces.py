# http://www.codewars.com/kata/583203e6eb35d7980400002a/train/python
from re import findall


def count_smileys(arr):
    counter = 0
    eyes = [':', ';']
    nose = ['-', '~', '']
    mouth = [')', 'D']

    for smile in arr:
        if len(smile) == 3:
            if (smile[0] in eyes) and (smile[1] in nose) and (smile[-1] in mouth):
                counter += 1
        elif len(smile) == 2:
            if (smile[0] in eyes) and (smile[-1] in mouth):
                counter += 1

    return counter


def count_smileys_regex(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))