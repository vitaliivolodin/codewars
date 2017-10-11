# https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python

def first_non_repeating_letter(string):
    strng = {}

    for i in string.lower():
        if i not in strng:
            strng[i] = 1
        else:
            strng[i] += 1

    for i in string.lower():
        if strng[i] == 1:
            return string[string.lower().index(i)]
            break
    else:
        return ''


if __name__ == '__main__':
    print(first_non_repeating_letter('sTreSS'))