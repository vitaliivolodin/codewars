# https://www.codewars.com/kata/permutations/train/python
import itertools


def permutations(string):
    permutation = list(map(list, list(set(itertools.permutations(string, len(string))))))

    return [''.join(x) for x in permutation]


if __name__ == '__main__':
    print(permutations('a'))
    print(permutations('ab'))
    print(permutations('aabb'))