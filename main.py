from translator_b import translate_to_roman
from translator_b import translate_to_decimal
from translator_a import show
from validation import valid


# Input
number = input('Give me a number (roman or decimal): ')
if number.isdigit():  # Decimal number to roman numeral
    if not valid(eval(number)):
        result = "It must be an integer number between 1 and 3999"
    else:
        result = translate_to_roman(eval(number))
else:  # Roman numeral to decimal number
    result = translate_to_decimal(number.upper())


# Output
print(result)
