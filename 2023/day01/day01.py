import re
import aocd


def find_digits_in_string(line):
    # Mapping of text to digits
    text_to_digit = {
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

    # Initialize an empty list to store digits
    digits = []

    # Sort keys by length in descending order to match longest text first
    sorted_keys = sorted(text_to_digit.keys(), key=len, reverse=True)

    # Regular expression to match both numeral digits and text digits
    pattern = r"\d|(?:" + "|".join(sorted_keys) + r")"

    # Use a while loop to iteratively find and replace matches
    index = 0
    while index < len(line):
        match = re.search(pattern, line[index:])
        if not match:
            break
        matched_text = match.group()
        # If the match is a text representation, convert it to a digit
        if matched_text in text_to_digit:
            digits.append(text_to_digit[matched_text])
        else:
            # Otherwise, it's already a numeral digit
            digits.append(matched_text)
        # Move the index forward by the length of the matched text
        index += match.start() + 1

    if len(digits) == 0:
        return 0

    if len(digits) == 1:
        return int(digits[0] + digits[0])

    return int(digits[0] + digits[-1])


def calculate_sum(input_lines):
    sum = 0
    line_number = 0
    with open("debug_output.txt", "w") as debug_file:  # Open a file for writing
        for line in input_lines:
            result = find_digits_in_string(line)
            sum += result
            line_number += 1
            debug_file.write(  # Write to the file instead of printing
                f"Line {line_number}: {line}, Result: {result}, Sum: {sum}\n"
            )

    return sum


# Test for part 1
input_lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

value_list = []

for line in input_lines:
    value_list.append(find_digits_in_string(line))

assert list(value_list) == [12, 38, 15, 77]
assert calculate_sum(input_lines) == 142

# Test for part 2
input_lines_2 = [
    "crvhlfone7xsqhkshpsix2nine73oneighttq",
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]

value_list = []

for line in input_lines_2:
    result = find_digits_in_string(line)
    # print(f"Line: {line}, Result: {result}")  # Debugging output
    value_list.append(result)

assert list(value_list) == [18, 29, 83, 13, 24, 42, 14, 76]
assert calculate_sum(input_lines_2) == 299

# get the input from advent of code
input_lines = aocd.get_data(day=1, year=2023).splitlines()

# Read input lines from a text file
# with open("day01/input.txt", "r") as file:
#     input_lines = file.readlines()

# Calculate sum
sum = calculate_sum(input_lines)
print(f"Sum: {sum}")
