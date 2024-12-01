import re
import aocd


def calculate_sum_of_differences(first_list, second_list):
    return sum(abs(first - second) for first, second in zip(first_list, second_list))


def split_input_into_lists(input_lines):
    list1 = []
    list2 = []
    for line in input_lines:
        numbers = list(map(int, line.split()))
        if len(numbers) >= 2:
            list1.append(numbers[0])
            list2.append(numbers[1])
    return list1, list2


def count_equal_numbers(first_list, second_list):
    counts = []
    for number in first_list:
        count = second_list.count(number)
        counts.append(count * number)
    return counts


# Test for part 1
first_list = [3, 4, 2, 1, 3, 3]
second_list = [4, 3, 5, 3, 9, 3]

# Calculate the difference between corresponding items in the lists
sum_of_differences = sum(
    abs(first - second)
    for first, second in zip(sorted(first_list), sorted(second_list))
)

assert sum_of_differences == 11

# Test for part 2
similarity_scores = count_equal_numbers(first_list, second_list)
assert sum(similarity_scores) == 31

# get the input from advent of code
input_lines = aocd.get_data(day=1, year=2024).splitlines()

first_list, second_list = split_input_into_lists(input_lines)

sum_of_differences = calculate_sum_of_differences(
    sorted(first_list), sorted(second_list)
)

print(f"Sum of differences: {sum_of_differences}")

similarity_scores = count_equal_numbers(first_list, second_list)
print(f"Sum of similarity scores: {sum(similarity_scores)}")
