
ROMAN_10 = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X')
ROMAN_100 = ('X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', 'C')


def translate(number):
    first_place = number - 10
    second_place = number // 10

    result = ROMAN_100[second_place - 1] + ROMAN_10[first_place - 1]

    return result


def show(limit):

    for i in range(limit):
        if i < 10:
            result = ROMAN_10[i]
        else:
            result = ROMAN_100[i // 10 - 1] + ROMAN_10[i - (i // 10) * 10]
        print(i + 1, result)
