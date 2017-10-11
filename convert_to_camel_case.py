# http://www.codewars.com/kata/517abf86da9663f1d2000003/train/python


def to_camel_case(text):
    split_symbol = '_'
    text = text.replace('-', '_')

    text = text.split(split_symbol)
    return ''.join([text[x] if x == 0 else text[x].capitalize() for x in range(len(text))])


if __name__ == '__main__':
    # returns "theStealthWarrior"
    print(to_camel_case("the_stealth_warrior"))

    # returns "TheStealthWarrior"
    print(to_camel_case("The_Stealth_Warrior"))