
TO_ROMAN = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
TO_DECIMAL = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# Input
# number = eval(input('Give me a number: '))
number = 5

one = TO_ROMAN[1]
five = TO_ROMAN[5]
result = ''
repeated = 0

for i in range(number):
    if repeated < 3:
        result = result + one
        repeated += 1
    elif repeated == 3:
        result = one + five
        repeated += 1
    else:
        result = five
        repeated = 0

# Output
print(result)
