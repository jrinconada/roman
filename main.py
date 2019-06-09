from translator_b import translate_to_roman
from translator_b import translate_to_decimal
from translator_a import show
from validation import valid_number
from validation import valid_word
from validation import valid_letters


# Input
number = input('Give me a number (roman or decimal): ')
if number.isdigit():  # Decimal number to roman numeral
    if not valid_number(eval(number)):
        result = "It must be an integer number between 1 and 3999"
    else:
        result = translate_to_roman(eval(number))
elif not valid_word(number):  # Roman numeral to decimal number
    result = "Invalid letter, must be one of these: " + valid_letters()
else:
    result = translate_to_decimal(number.upper())


# Output
print(result)
