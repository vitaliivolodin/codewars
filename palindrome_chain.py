# http://www.codewars.com/kata/525f039017c7cd0e1a000a26/train/python


def palindrome_chain_length(n):
    counter = 0
    number = n
    while number != int(str(number)[::-1]):
        number += int(str(number)[::-1])
        counter += 1

    return counter


if __name__ == '__main__':
    print(palindrome_chain_length(87))