# https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python
import re


def is_valid_ip(strng):
    strng = strng.split('.')

    if len(strng) != 4:
        return False

    for i in strng:
        try:
            if len(i) > 1:
                if i[0] == '0':
                    return False
            if int(i) > 255 or int(i) < 0:
                return False
            if ' ' in i:
                return False

        except ValueError:
            return False

    return True


# REGEX solution
def is_valid_ip_regex(strng):
    return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)', strng))


if __name__ == '__main__':
    print(is_valid_ip('255.255.25 .255'))