import re
import aocd


def is_safe_line(line):
    increasing = True
    decreasing = True
    differences_within_limit = True

    for x, y in zip(line, line[1:]):
        if x >= y:
            increasing = False
        if x <= y:
            decreasing = False
        if abs(x - y) > 3:
            differences_within_limit = False

    return (increasing or decreasing) and differences_within_limit


def is_safe_line_part2(line):
    # Check if the original line is safe
    if is_safe_line(line):
        return True

    # Check if removing one number makes the line safe
    for i in range(len(line)):
        if is_safe_line(line[:i] + line[i + 1 :]):  # exclude the number at index i
            return True

    return False


# Test for part 1
reports_strings = [
    "7 6 4 2 1",
    "1 2 7 8 9",
    "9 7 6 2 1",
    "1 3 2 4 5",
    "8 6 4 4 1",
    "1 3 6 7 9",
]

# Use regular expressions to split each line into numbers
reports_array = [list(map(int, re.findall(r"\d+", line))) for line in reports_strings]

safe_lines = [line for line in reports_array if is_safe_line(line)]
assert len(safe_lines) == 2

# Test for part 2
safe_lines = [line for line in reports_array if is_safe_line_part2(line)]
assert len(safe_lines) == 4

# get the input from advent of code
reports_strings = aocd.get_data(day=2, year=2024).splitlines()

# Use regular expressions to split each line into numbers
reports_array = [list(map(int, re.findall(r"\d+", line))) for line in reports_strings]

safe_lines = [line for line in reports_array if is_safe_line(line)]

print("Number of safe lines:", len(safe_lines))

safe_lines = [line for line in reports_array if is_safe_line_part2(line)]
print("Number of safe lines part 2:", len(safe_lines))
