
TO_ROMAN = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
TO_DECIMAL = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def to_roman(number, unit, half, top):
    result = ''
    repeated = 0

    for i in range(number):
        if repeated < 3:  # I, II, III and VI, VII, VIII
            result = result + unit
            repeated += 1
        elif repeated == 3:  # IV and IX
            result = unit + half
            repeated += 1
        elif repeated == 4:  # V and X
            result = half
            half = top
            repeated = 0
    return result


def translate(number):
    result = ''

    remains = number // 10
    result = to_roman(remains, TO_ROMAN[10], TO_ROMAN[50], TO_ROMAN[100])
    result += to_roman(number - 10, TO_ROMAN[1], TO_ROMAN[5], TO_ROMAN[10])

    return result
