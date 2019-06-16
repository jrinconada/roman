

# For validation
VALID_LETTERS = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
FIVE_BASED = ('V', 'L', 'D')
VALID_SUBTRACTIONS = ('IV', 'IX', 'XL', 'XC', 'CD', 'CM')

# For translation A
ROMAN_10 = ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X')
ROMAN_100 = ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C')
ROMAN_1000 = ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', 'M')
ROMAN_10000 = ('', 'M', 'MM', 'MMM')

# For translation B
TO_ROMAN = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 5000: '', 10000: ''}
TO_DECIMAL = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
