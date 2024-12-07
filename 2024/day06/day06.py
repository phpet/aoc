import aocd

map = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#...",
]


def move_through_map(map_matrix):
    # Find the initial position of the guard
    position = None
    for i, row in enumerate(map_matrix):
        if "^" in row:
            position = (i, row.index("^"))
            break

    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_direction = 0  # Start facing up

    # Mark the initial position
    map_matrix[position[0]][position[1]] = "X"

    while True:
        # Calculate the next position
        next_position = (
            position[0] + directions[current_direction][0],
            position[1] + directions[current_direction][1],
        )

        # Check if the next position is out of bounds
        if (
            next_position[0] < 0
            or next_position[0] >= len(map_matrix)
            or next_position[1] < 0
            or next_position[1] >= len(map_matrix[0])
        ):
            break

        # Check if the next position is an obstacle
        if map_matrix[next_position[0]][next_position[1]] == "#":
            # Turn right
            current_direction = (current_direction + 1) % 4
        else:
            # Move to the next position
            position = next_position
            # Mark the path
            map_matrix[position[0]][position[1]] = "X"

    return map_matrix


def move_through_map2(map_matrix, max_steps=10000):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_direction = 0  # Start facing up

    # Find the starting position of the guard
    position = None
    for i, row in enumerate(map_matrix):
        if "^" in row:
            position = (i, row.index("^"))
            break

    visited = set()
    steps = 0

    while True:
        # Mark the current position and direction
        visited.add((position, current_direction))
        steps += 1
        if steps > max_steps:
            return False  # Prevent infinite looping

        # Calculate the next position
        next_position = (
            position[0] + directions[current_direction][0],
            position[1] + directions[current_direction][1],
        )

        # Check for out-of-bounds
        if (
            next_position[0] < 0
            or next_position[0] >= len(map_matrix)
            or next_position[1] < 0
            or next_position[1] >= len(map_matrix[0])
        ):
            return False  # Exited the map

        # Detect a loop
        if (next_position, current_direction) in visited:
            return True

        # Handle obstacles
        if map_matrix[next_position[0]][next_position[1]] == "#":
            current_direction = (current_direction + 1) % 4
        else:
            position = next_position


# Finds positions where adding an obstacle creates a loop
def find_obstacle_positions(map):
    loop_positions = []
    loop_count = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == ".":
                map_matrix = [list(row) for row in map]
                map_matrix[i][j] = "#"
                if move_through_map2(map_matrix):
                    loop_positions.append((i, j))
                    loop_count += 1
    return loop_count


# Test for part 1
map_matrix = [list(row) for row in map]
marked_map = move_through_map(map_matrix)
assert sum(row.count("X") for row in marked_map) == 41

# get the input from advent of code
map = aocd.get_data(day=6, year=2024).splitlines()

# Part 1
map_matrix = [list(row) for row in map]
marked_map = move_through_map(map_matrix)
loop_count = sum(row.count("X") for row in marked_map)
print("loop_count 1:", loop_count)

# Part 2
loop_count = find_obstacle_positions(map)
print("loop_count 2:", loop_count)
