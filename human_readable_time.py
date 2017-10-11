# http://www.codewars.com/kata/52685f7382004e774f0001f7/train/python


def make_readable(seconds):
    hours = int(seconds / 3600)
    minutes = int((seconds % 3600) / 60)
    seconds = int(((seconds % 3600) % 60))

    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)


if __name__ == '__main__':
    print(make_readable(0))