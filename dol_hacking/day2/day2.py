import os
import itertools
import more_itertools
import collections
from contextlib import contextmanager

# Reference: https://adventofcode.com/2018/day/2

@contextmanager
def get_input_data():
    input_file_path =  os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file_path, mode='r') as input_file:
        yield input_file

def process_box_id1(string):
    dictionary = {}
    for letter in string:
        dictionary[letter] = dictionary.get(letter, 0) + 1

    return dictionary

def has_n_duplicates(dictionary, n):
    for k, v in dictionary.items():
        if v == n:
            return True

    return False

def process_line1a(line):
    dictionary = process_box_id1(line)
    return has_n_duplicates(dictionary, 2), has_n_duplicates(dictionary, 3)

def process_line1(line):
    counts = collections.Counter(line).values()
    return 2 in counts, 3 in counts

def process_data1(data):
    duplicates = 0
    triplicates = 0
    for line in data:
        duplicate, triplicate = process_line1(line)

        if duplicate:
            duplicates += 1

        if triplicate:
            triplicates += 1

    return duplicates * triplicates

def find_close_match(data):
    combinations = itertools.combinations(data, 2)
    for left_id, right_id in combinations:
        matches = [left_char!=right_char for left_char, right_char in zip(left_id, right_id)]

        if sum(matches) == 1:
            return left_id, right_id

    return None, None

def process_data2(data):
    left, right = find_close_match(data)
    return "".join([left_char for left_char, right_char in zip(left, right) if left_char == right_char])

def run():
    with get_input_data() as data:
        answer1 = process_data1(data)
        print(f"The answer to part 1 is: {answer1}")

    with get_input_data() as data:
        answer2 = process_data2(data)
        print(f"The answer to part 2 is: {answer2}")

if __name__ == "__main__":
    run()