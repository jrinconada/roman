
TO_ROMAN = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
TO_DECIMAL = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# Input
# number = eval(input('Give me a number: '))
number = 8

one = TO_ROMAN[1]
limit = TO_ROMAN[5]
result = ''
repeated = 0

for i in range(number):
    if repeated < 3:  # I, II, III and VI, VII, VIII
        result = result + one
        repeated += 1
    elif repeated == 3:  # IV and IX
        result = one + limit
        repeated += 1
    elif repeated == 4:  # V and X
        result = limit
        limit = TO_ROMAN[10]
        repeated = 0

# Output
print(result)
