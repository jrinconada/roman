
VALID_LETTERS = ('I', 'V', 'X', 'L', 'C', 'D', 'M')

def valid_number(user_input):
    """ Returns True if input is an integer number between 1 and 3999 """
    return 1 <= user_input <= 3999


def valid_word(user_input=''):
    """ Returns True if all letters are valid roman numerals """
    user_input = user_input.upper()
    for letter in VALID_LETTERS:  # Removes all the roman numerals letters
        user_input = user_input.replace(letter, '')
    return not user_input  # If user input is empty all the letters were roman numerals


def valid_letters():
    """ Returns a human readable list for the valid roman numerals """
    valids = ''
    for letter in VALID_LETTERS[:-2]:
        valids += letter + ', '
    valids += VALID_LETTERS[-2] + ' or ' + VALID_LETTERS[-1]
    return valids
