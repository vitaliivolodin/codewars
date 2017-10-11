# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python


def move_zeros(array):
    return sorted(array, key=lambda x: (x == 0) and x is not False)


if __name__ == '__main__':
    print(move_zeros([1, 2, 0.0, 1, 0, 1, 0, 3, 0, 1]))
    print(move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
    print(move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]))