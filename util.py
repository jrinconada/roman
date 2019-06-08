

def get_digit(number, digit):
    digit_sum = 0
    for i in range(digit):
        digit_sum += number - ((number // 10**(i+1)) * 10**(i+1) + digit_sum)
    return digit_sum // 10**(digit-1)


def get_digit_b(number, digit):
    return number % 10**digit // 10**(digit-1)


def get_digit_c(number, digit):
    return int(str(number)[-digit])
