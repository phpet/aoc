import aocd

data = [
    "190: 10 19",
    "3267: 81 40 27",
    "83: 17 5",
    "156: 15 6",
    "7290: 6 8 6 15",
    "161011: 16 10 13",
    "192: 17 8 14",
    "21037: 9 7 18 13",
    "292: 11 6 16 20",
]

operation = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
    "|": lambda x, y: int(str(x) + str(y)),
}


def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = operation[operators[i - 1]](result, numbers[i])
    return result


def generate_op_combinations(n, part):
    if part == 1:
        operators = "+*"
    else:
        operators = "+*|"

    if n == 0:
        return [""]

    # run recursively
    smaller_combinations = generate_op_combinations(n - 1, part)

    # generate all combinations
    combinations = []
    for op in operators:
        for comb in smaller_combinations:
            combinations.append(op + comb)

    return combinations


def find_combination(key, values_list, part=1):
    operator_combinations = generate_op_combinations(len(values_list) - 1, part)

    for ops in operator_combinations:
        if evaluate_expression(values_list, ops) == key:
            print(f"Values {values_list} and operators {ops} = {key}")
            return True
    return False


# Split the data into lines and parse each line
array = []
for line in data:
    key, values = line.split(":")
    values_list = list(map(int, values.split()))
    array.append((int(key), values_list))

# Test for part 1
sum = 0

for key, values_list in array:
    if find_combination(key, values_list):
        sum += key

assert sum == 3749

# get the input from advent of code
data = aocd.get_data(day=7, year=2024).splitlines()

array = []
for line in data:
    key, values = line.split(":")
    values_list = list(map(int, values.split()))
    array.append((int(key), values_list))

# Part 1
sum = 0

for key, values_list in array:
    if find_combination(key, values_list):
        sum += key

print("Part 1:", sum)

# Part 2
sum = 0

for key, values_list in array:
    if find_combination(key, values_list, part=2):
        sum += key

print("Part 2:", sum)
