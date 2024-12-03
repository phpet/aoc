import re
import aocd

multiplication_enabled = True


def calculate_multiplications(memory_string):
    global multiplication_enabled
    multiplications = []

    for match in re.finditer(r"mul\((\d+),(\d+)\)|don't\(\)|do\(\)", memory_string):
        if match.group(0).startswith("don't"):
            multiplication_enabled = False
        elif match.group(0).startswith("do"):
            multiplication_enabled = True
        elif multiplication_enabled and match.group(0).startswith("mul"):
            x, y = match.groups()
            multiplications.append(int(x) * int(y))

    return sum(multiplications)


# Test for part 1
memory_string = (
    "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
)

instructions = re.findall(r"mul\((\d+),(\d+)\)", memory_string)
multiplications = [int(x) * int(y) for x, y in instructions]
assert sum(multiplications) == 161

# Test for part 2
memory_string = (
    "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
)

assert calculate_multiplications(memory_string) == 48

# get the input from advent of code
reports_strings = aocd.get_data(day=3, year=2024).splitlines()

# Solution for part 1
total_multiplications = 0

for line in reports_strings:
    instructions = re.findall(r"mul\((\d+),(\d+)\)", line)
    multiplications = [int(x) * int(y) for x, y in instructions]
    total_multiplications += sum(multiplications)

print("Sum of multiplications (part 1):", total_multiplications)

# Solution for part 2
total_multiplications = 0
multiplication_enabled = True

for line in reports_strings:
    total_multiplications += calculate_multiplications(line)

print("Sum of multiplications (part 2):", total_multiplications)
