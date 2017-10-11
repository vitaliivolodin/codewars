# https://www.codewars.com/kata/52de553ebb55d1fca3000371/train/python


def find_missing(sequence):
    full_sequence = set(range(sequence[0], sequence[-1], sequence[1] - sequence[0]))
    return (full_sequence - set(sequence)).pop()


if __name__ == '__main__':
    print(find_missing([1, 2, 3, 4, 6, 7, 8, 9]))

