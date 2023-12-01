from string import digits
from pipe import map
from re import finditer

with open("./input.txt") as input_fp:
    input_data = input_fp.read().splitlines()

##################
#### PART - 1 ####
##################

def extract_calibration_value(text_line):
    numerics = [
        character
        for character in text_line
        if character in digits
    ]

    return int(numerics[0] + numerics[-1])


calibration_sum = sum( input_data | map(extract_calibration_value) )
print(calibration_sum)


##################
#### PART - 2 ####
##################

spelled_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

with open("./input.txt") as input_fp:
    input_data = input_fp.read().splitlines()

def find_first_digit_occurence(line):
    for index, character in enumerate(line):
        if character in digits:
            return index, character
    return None, None


def find_all_occurences(pattern, line):
    return [
        i.start()
        for i in finditer(pattern, line)
    ]

def check_digit(substr: str, reversed=False):
    if substr[0].isdigit():
        return substr[0]

    for spelling, digit in spelled_digits.items():
        spelling = spelling if not reversed else spelling[::-1]
        if substr.startswith(spelling):
            return digit
    return None



def get_calibration_value_2(line):
    for i in range(0, len(line)):
        digit_1 = check_digit(line[i::], False)
        if digit_1:
            break

    reversed_line = line[::-1]
    for i in range(0, len(reversed_line)):
        digit_2 = check_digit(reversed_line[i::], True)
        if digit_2:
            break

    return int(digit_1 + digit_2)

print(sum(
    get_calibration_value_2(line)
    for line in input_data
))
