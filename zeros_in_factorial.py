# https://www.codewars.com/kata/number-of-trailing-zeros-of-n/train/python


def zeros_math(n):
    i = 5
    zeros = 0

    while n >= i:
        zeros += n // i
        i *= 5
    return zeros

if __name__ == '__main__':
    print(zeros_math(5))
    print(zeros_math(30))

