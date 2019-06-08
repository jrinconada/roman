

def get_digit(number, digit):
    sum = 0
    for i in range(digit):
        sum += number - ((number // 10**(i+1)) * 10**(i+1) + sum)
    return sum // 10**(digit-1)
