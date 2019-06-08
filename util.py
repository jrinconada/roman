

def get_digit(number, digit):
    """ Given a number, returns the digit in the specified position, for an out of range digit returns 0 """
    digit_sum = 0
    for i in range(digit):  # Accumulate all the other digits and subtract from the original number
        digit_sum += number - ((number // 10**(i+1)) * 10**(i+1) + digit_sum)
    return digit_sum // 10**(digit-1)


def get_digit_b(number, digit):
    """ Given a number, returns the digit in the specified position, for an out of range digit returns 0 """
    return number % 10**digit // 10**(digit-1)  # Shortest mathematical method (module and integer division)


def get_digit_c(number, digit):
    """ Given a number, returns the digit in the specified position, does not accept out of range digits """
    return int(str(number)[-digit])  # Simplest method by casting to string and access by index
