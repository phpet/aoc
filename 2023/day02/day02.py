import re
import aocd


def calculate_sum(possible_games):
    sum = 0

    for game in possible_games:
        sum += game

    return sum


def calculate_power(max_cubes):
    return max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]


def is_possible_game(line):
    # The number of cubes for each color
    cubes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    # Initialize a dictionary to store the maximum number for each color
    max_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    # Regular expression to find numbers followed by a color
    pattern = r"(\d+)\s+(red|green|blue)"

    # Find all matches in the line
    matches = re.findall(pattern, line)

    for number, color in matches:
        number = int(number)
        # Update the maximum number for each color
        if number > max_cubes[color]:
            max_cubes[color] = number

    power = calculate_power(max_cubes)

    is_possible = True

    # Compare the maximum numbers with the cubes dictionary
    for color in cubes:
        if cubes[color] < max_cubes[color]:
            is_possible = False
            break

    return is_possible, power


# Test for part 1
input_lines = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

possible_games = []
sum_of_powers = 0

for index, line in enumerate(input_lines, start=1):
    is_possible, power = is_possible_game(line)
    sum_of_powers += power

    if is_possible:
        possible_games.append(index)

assert list(possible_games) == [1, 2, 5]
assert calculate_sum(possible_games) == 8
assert sum_of_powers == 2286

# get the input from advent of code
input_lines = aocd.get_data(day=2, year=2023).splitlines()

possible_games = []
sum_of_powers = 0

for index, line in enumerate(input_lines, start=1):
    is_possible, power = is_possible_game(line)
    sum_of_powers += power

    if is_possible:
        possible_games.append(index)

# Calculate sum
sum = calculate_sum(possible_games)
print(f"Sum: {sum}")
print(f"Powers: {sum_of_powers}")
