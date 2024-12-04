import re
import aocd

# test matrix
matrix = [
    list("MMMSXXMASM"),
    list("MSAMXMSMSA"),
    list("AMXSXMAAMM"),
    list("MSAMASMSMX"),
    list("XMASAMXAMM"),
    list("XXAMMXXAMA"),
    list("SMSMSASXSS"),
    list("SAXAMASAAA"),
    list("MAMMMXMMMM"),
    list("MXMXAXMASX"),
]


def find_word_in_matrix(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    word_length = len(word)

    def check_direction(r, c, dr, dc):
        for i in range(word_length):
            nr = r + i * dr
            nc = c + i * dc
            if (
                nr < 0
                or nr >= rows
                or nc < 0
                or nc >= cols
                or matrix[nr][nc] != word[i]
            ):
                return False
        return True

    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (1, 1),  # down-right
        (1, -1),  # down-left
        (0, -1),  # left
        (-1, 0),  # up
        (-1, -1),  # up-left
        (-1, 1),  # up-right
    ]

    count = 0

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if check_direction(r, c, dr, dc):
                    count += 1

    return count


def find_2_diagonal_words_in_matrix(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    word_length = len(word)

    def check_direction(r, c, dr, dc, reverse=False):
        for i in range(word_length):
            nr = r + i * dr
            nc = c + i * dc
            char_index = i

            if reverse:
                char_index = word_length - i - 1

            if (
                nr < 0
                or nr >= rows
                or nc < 0
                or nc >= cols
                or matrix[nr][nc] != word[char_index]
            ):
                return False  # word not found in this direction

        return True  # word found in this direction

    count = 0

    for r in range(rows):
        for c in range(cols):
            # check down-right
            found_down_right = check_direction(r, c, 1, 1) or check_direction(
                r, c, 1, 1, reverse=True
            )

            # check down-left
            found_down_left = check_direction(r, c + 2, 1, -1) or check_direction(
                r, c + 2, 1, -1, reverse=True
            )

            if found_down_right and found_down_left:
                count += 1

    return count


# Test for part 1
assert find_word_in_matrix(matrix, "XMAS") == 18

# Test for part 2
assert find_2_diagonal_words_in_matrix(matrix, "MAS") == 9

# get the input from advent of code
data = aocd.get_data(day=4, year=2024).splitlines()
matrix = [list(line) for line in data]

# Solution for part 1
print("Part 1:", find_word_in_matrix(matrix, "XMAS"))

# Solution for part 2
print("Part 2:", find_2_diagonal_words_in_matrix(matrix, "MAS"))
