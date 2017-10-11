def persistence(n):
    result = 0
    number = n

    while len(str(number)) > 1:
        multiply = 1
        if len(str(number)) == 1:
            return 0
        else:
            number_list = [int(x) for x in str(number)]
            for i in number_list:
                multiply *= i
                number = multiply
            result += 1

    return result


if __name__ == '__main__':
    print(persistence(999))
