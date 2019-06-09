from util import get_digit


TO_ROMAN = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 5000: '', 10000: ''}
EQUIVALENCES_TO_10 = {'I': 1, 'V': 5, 'X': 10}
EQUIVALENCES_TO_100 = {'X': 10, 'L': 50, 'C': 100}
EQUIVALENCES_TO_1000 = {'C': 100, 'D': 500, 'M': 1000}


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
    decimal = to_decimal(roman, EQUIVALENCES_TO_10)
    return decimal


def to_decimal(roman, equivalent):
    result = 0
    previous = 0
    for letter in roman:  # Starting in the second element
        if equivalent[letter] <= previous:  # Adding if I, II, III, V, VI, VII, VIII or X
            result += equivalent[letter]
        else:  # Subtracting if IV or IX
            result += equivalent[letter] - 2 * previous  # Must subtract the current unit and the previously added
        previous = equivalent[letter]

    return result
