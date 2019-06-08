from util import get_digit


ROMAN_10 = ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X')
ROMAN_100 = ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C')
ROMAN_1000 = ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', 'M')
ROMAN_10000 = ('', 'M', 'MM', 'MMM')


def translate(number):
    return ROMAN_10000[get_digit(number, 4)] + \
           ROMAN_1000[get_digit(number, 3)] + \
           ROMAN_100[get_digit(number, 2)] + \
           ROMAN_10[get_digit(number, 1)]


def show(limit):
    for i in range(1, limit + 1):
        result = ROMAN_10000[get_digit(i, 4)] + \
                 ROMAN_1000[get_digit(i, 3)] + \
                 ROMAN_100[get_digit(i, 2)] + \
                 ROMAN_10[get_digit(i, 1)]
        print(i, result)
