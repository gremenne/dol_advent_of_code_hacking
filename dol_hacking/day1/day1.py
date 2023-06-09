import os
import itertools
import more_itertools
from contextlib import contextmanager

@contextmanager
def get_input_data():
    input_file_path =  os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file_path, mode='r') as input_file:
        yield input_file

def process_data1_first_try(data):
    sum = 0
    for line in data:
        sum +=int(line)

    return sum

def process_data1(data):
    return sum([int(line) for line in data])

def process_data2_first_try(data):
    sum = 0
    seen = set([0])
    while True:
        for line in data:
            sum +=int(line)
            if sum in seen:
                return sum
            seen.add(sum)

def process_data2_second_try(data):
    seen = set([0])
    for value in itertools.accumulate(itertools.cycle([int(line) for line in data])):
        if value in seen:
            return value
        seen.add(value)

def process_data2(data):
    value = more_itertools.first(
        more_itertools.duplicates_everseen(
        itertools.accumulate(
        itertools.chain(
            [0],
            itertools.cycle([int(line) for line in data])))))

    return value

def day1():
    with get_input_data() as data:
        answer1 = process_data1(data)
        print(f"The answer to part 1 is: {answer1}")

    with get_input_data() as data:
        answer2 = process_data2(data)
        print(f"The answer to part 2 is: {answer2}")

if __name__ == "__main__":
    day1()