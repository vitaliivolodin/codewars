def get_middle(s):
    if len(s) % 2 == 1:
        return s[int(len(s) / 2)]
    else:
        return s[:int(len(s) / 2)][-1] + s[int(-len(s) / 2):][0]


if __name__ == '__main__':
    print(get_middle('textsd'))