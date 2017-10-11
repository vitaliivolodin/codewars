def dig_pow(n, p):
    n = int(n)
    p = int(p)

    number_list = [int(x) for x in str(n)]
    power_list = list(range(p, p + len(number_list)))
    result = 0

    L = list(zip(number_list, power_list))

    for a, b in L:
        result += (a ** b)

    if (result % n) == 0:
        return result / n
    else:
        return -1


if __name__ == '__main__':
    print(dig_pow(3263, 4))