# https://www.codewars.com/kata/largest-5-digit-number-in-a-series/train/python


def solution(digits):
    start, end = 0, 5
    numbers = []
    for i in range(len(digits) - 2):
        if len(digits[start:end]) == 5:
            numbers.append(digits[start:end])
            start += 1
            end += 1

    return int(max(numbers))


if __name__ == '__main__':
    print(solution('7653147235748123765231748652347165234183'))