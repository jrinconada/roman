from translator_a import translate
from translator_a import show
from validation import valid


# Input
number = input('Give me a number: ')
if not number.isdigit() or not valid(eval(number)):
    print("It must be an integer number between 1 and 3999")
    quit()

# Translation
result = translate(eval(number))

# Output
print(result)
