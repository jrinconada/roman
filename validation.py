from constants import VALID_LETTERS
from constants import FIVE_BASED
from constants import TO_DECIMAL
from constants import VALID_SUBTRACTIONS


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


# Strict rules
def no_more_than_three(number=''):
    """ Returns True if there are no more than three consecutive numerals """
    prev = ''
    counter = 0
    for letter in number:
        if prev == letter:
            counter += 1
        else:
            counter = 1
        if counter > 3:
            return False
        prev = letter

    return True


def no_more_than_one(number=''):
    """ Returns True if there are no more than one 5 based numeral """
    prev = ''
    repetitions = 0
    for letter in number:
        if prev == letter and letter in FIVE_BASED:
            repetitions += 1
        else:
            repetitions = 0
        if repetitions >= 1:
            return False
        prev = letter

    return True
