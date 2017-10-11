# https://www.codewars.com/kata/5264d2b162488dc400000001


def spin_words(sentence):
    result = [x[::-1] if len(x) >= 5 else x for x in sentence.split()]

    return ' '.join(result)


if __name__ == '__main__':
    print(spin_words('This is another test'))