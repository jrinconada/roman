from util import get_digit
from constants import TO_DECIMAL
from constants import TO_ROMAN


def to_roman(number, unit, half, top):
    """ Given a digit and the range is on (unit, half, top) it is on adds as many roman numerals as necessary
        Sample call: to_roman(8, 'I', 'V', 'X') -> 'VIII'
    """
    result = ''
    repeated = 0

    for i in range(number):
        if repeated < 3:  # I, II, III and VI, VII, VIII
            result = result + unit
            repeated += 1
        elif repeated == 3:  # IV and IX
            result = unit + half
            repeated += 1
        elif repeated == 4:  # V and X
            result = half
            half = top
            repeated = 0
    return result


def translate_to_roman(number):
    """ Given a number between 1 and 3999 returns the equivalent roman numeral """
    result = ''

    for i in reversed(range(1, 5)):  # Run the function for every range of roman numerals
        result += to_roman(get_digit(number, i), TO_ROMAN[10**(i-1)], TO_ROMAN[10**(i-1) * 5], TO_ROMAN[10**i])

    return result


def translate_to_decimal(roman):
    """ Given a roman numeral returns the equivalent in decimal number system """
    decimal = to_decimal(roman)
    return decimal


def to_decimal(roman):
    result = 0
    previous = 0
    for letter in roman:  # Starting in the second element
        if TO_DECIMAL[letter] <= previous:  # Adding if I, II, III, V, VI, VII, VIII or X
            result += TO_DECIMAL[letter]
        else:  # Subtracting if IV or IX
            result += TO_DECIMAL[letter] - 2 * previous  # Must subtract the current unit and the previously added
        previous = TO_DECIMAL[letter]

    return result
