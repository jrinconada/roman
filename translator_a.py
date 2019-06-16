from util import get_digit
from constants import ROMAN_10
from constants import ROMAN_100
from constants import ROMAN_1000
from constants import ROMAN_10000


def translate(number):
    """ Given a number between 1 and 3999 returns the equivalent roman numeral """
    # Gets the proper combination for every digit
    return ROMAN_10000[get_digit(number, 4)] + \
        ROMAN_1000[get_digit(number, 3)] + \
        ROMAN_100[get_digit(number, 2)] + \
        ROMAN_10[get_digit(number, 1)]


def show(limit):
    """ Prints all the roman numerals from 1 to a given limit """
    for i in range(1, limit + 1):
        result = ROMAN_10000[get_digit(i, 4)] + \
                 ROMAN_1000[get_digit(i, 3)] + \
                 ROMAN_100[get_digit(i, 2)] + \
                 ROMAN_10[get_digit(i, 1)]
        print(i, result)
