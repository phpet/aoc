import aocd

# Test Input pairs
pairs = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
]

# Test Input sequences
sequences = [
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47",
]


def is_sequence_valid(sequence, int_pairs):
    for i in range(len(sequence) - 1):
        if [sequence[i], sequence[i + 1]] not in int_pairs:
            return False

    return True


def rearrange_sequence(sequence):
    # convert the list of pairs to a set of tuples
    valid_transitions = set(tuple(pair) for pair in int_pairs)

    # backtrack to find the valid sequence
    def backtrack(path, remaining):
        if not remaining:
            return path
        for i, num in enumerate(remaining):
            if not path or (path[-1], num) in valid_transitions:
                result = backtrack(path + [num], remaining[:i] + remaining[i + 1 :])
                if result:
                    return result
        return None

    return backtrack([], sequence)


def process_sequences(int_sequences, int_pairs):
    sum = 0  # sum of the middle numbers
    sum_r = 0  # sum of the middle numbers rearranged

    for seq in int_sequences:
        if is_sequence_valid(seq, int_pairs):
            print(f"Sequence {seq} is valid.")

            middle_index = len(seq) // 2
            middle_number = seq[middle_index]
            sum += middle_number
        else:
            print(f"Sequence {seq} is NOT valid.")

            rearranged_seq = rearrange_sequence(seq)

            middle_index = len(rearranged_seq) // 2
            middle_number = rearranged_seq[middle_index]
            sum_r += middle_number

            print(f"Rearranged sequence: {rearranged_seq}")

    return sum, sum_r


# Test for part 1

# Convert each pair in the list to a list of integers
int_pairs = [list(map(int, pair.split("|"))) for pair in pairs]

# Convert each sequence in the list to a list of integers
int_sequences = [list(map(int, seq.split(","))) for seq in sequences]

sum, sum2 = process_sequences(int_sequences, int_pairs)
assert sum == 143

# Test for part 2
assert sum2 == 123

# get the input from advent of code
data = aocd.get_data(day=5, year=2024).splitlines()

# Split the input data into pairs and sequences
split_index = data.index("")  # Find the index of the empty line
pairs_data = data[:split_index]
sequences_data = data[split_index + 1 :]

# Convert each pair in the list to a list of integers
int_pairs = [list(map(int, pair.split("|"))) for pair in pairs_data]

# Convert each sequence in the list to a list of integers
int_sequences = [list(map(int, seq.split(","))) for seq in sequences_data]

sum, sum2 = process_sequences(int_sequences, int_pairs)
print("Sum of middle numbers:", sum)
print("Sum of middle numbers rearranged:", sum2)
