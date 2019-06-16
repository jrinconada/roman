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
def more_than_three(number=''):
    """ Returns True if there are more than three consecutive numerals (ex: IIII) """
    prev = ''
    counter = 0
    for letter in number:
        if prev == letter:
            counter += 1
        else:
            counter = 1
        if counter > 3:
            return True
        prev = letter

    return False


def more_than_one_5(number=''):
    """ Returns True if there is more than one 5 based numeral (ex: VV) """
    prev = ''
    repetitions = 0
    for letter in number:
        if prev == letter and letter in FIVE_BASED:
            repetitions += 1
        else:
            repetitions = 0
        if repetitions >= 1:
            return True
        prev = letter

    return False


def invalid_subtractions(number=''):
    """ Returns True if there is an invalid subtraction (ex: IL, XM, VX) """
    prev = number[0]
    for letter in number[1:]:
        if TO_DECIMAL[prev] < TO_DECIMAL[letter] and (prev + letter) not in VALID_SUBTRACTIONS:
            return True
        prev = letter

    return False


def invalid_order(number=''):
    """ Returns True if there are smaller numbers before bigger ones
    and it is not a valid subtraction (ex: IC, IIV, VC, XDM) """
    for i in range(len(number)):
        letter = number[i]
        for j in range(i + 1, len(number)):
            if TO_DECIMAL[letter] < TO_DECIMAL[number[j]]:  # Invalid order unless it is a valid subtraction
                if not ((i == j - 1) and (letter + number[j]) in VALID_SUBTRACTIONS):
                    return True

    return False
