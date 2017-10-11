# http://www.codewars.com/kata/52774a314c2333f0a7000688/train/python


def valid_parentheses(string):
    string = ''.join([x for x in string if x in ['(', ')']])

    for i in range(int(len(string) / 2)):
        string = string.replace('()', '')

    return string == ''

if __name__ == '__main__':
    print(valid_parentheses('hi(hi)())'))