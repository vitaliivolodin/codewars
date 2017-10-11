# https://www.codewars.com/kata/next-bigger-number-with-the-same-digits/train/python


def next_bigger(n):
    string_n = str(n)
    pivot = -1
    substitute = None

    for i in range(len(string_n) - 1, -1, -1):
        if string_n[i] > string_n[i - 1]:
            pivot = i - 1
            break

    if pivot == -1:
        return -1

    left, right = string_n[:pivot], string_n[pivot + 1:]

    for i in sorted(right):
        if int(i) > int(string_n[pivot]):
            substitute = int(i)
            break

    right += string_n[pivot]
    right = ''.join(sorted(right.replace(str(substitute), '', 1)))

    return int(left + str(substitute) + right)


if __name__ == '__main__':
    print(next_bigger(12))
    print(next_bigger(513))
    print(next_bigger(21581957621))
    print(next_bigger(2017))
    print(next_bigger(144))