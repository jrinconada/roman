from translator_b import translate_to_roman
from translator_b import translate_to_decimal
from translator_a import show
from validation import valid_number
from validation import valid_word
from validation import valid_letters
from validation import more_than_one_5
from validation import more_than_three
from validation import invalid_subtractions
from validation import invalid_order


# Input
number = input('Give me a number (roman or decimal): ')

# Basic validation
to_roman = number.isdigit()
result = ''
if to_roman and not valid_number(eval(number)):  # Validate range
    result = 'It must be an integer number between 1 and 3999'
elif not valid_word(number):  # Validate letters
    result = 'Invalid letter, must be one of these: ' + valid_letters()

# Translation
if not result:
    if to_roman:  # Decimal number to roman numeral
        result = translate_to_roman(eval(number))
    else:  # Roman numeral to decimal number
        result = translate_to_decimal(number.upper())

# Strict roman numeral validation
if not to_roman:
    if more_than_three(number.upper()) or more_than_one_5(number.upper()) \
            or invalid_subtractions(number.upper()) or invalid_order(number.upper()):
        result = str(result) + ' (but it is not following the rules) it should be ' + translate_to_roman(result)

# Output
print(result)
