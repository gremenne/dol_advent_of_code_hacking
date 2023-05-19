import os
import itertools
import more_itertools

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

def dat1():
    input_file_path =  os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file_path, mode='r') as input_file:
        data = input_file.readlines()
        answer1 = process_data1(data)
        print(f"The answer to part 1 is: {answer1}")
        answer2 = process_data2(data)
        print(f"The answer to part 2 is: {answer2}")

def part1_tests():
    assert(process_data1(['+1', '-2', '+3', '+1']) == 3)
    assert(process_data1(['+1', '+1', '+1']) == 3)
    assert(process_data1(['+1', '+1', '-2']) == 0)
    assert(process_data1(['-1', '-2', '-3']) == -6)

def part2_tests():
    assert(process_data2(['+1', '-1']) == 0)
    assert(process_data2(['+3', '+3', '+4', '-2', '-4']) == 10)
    assert(process_data2(['-6', '+3', '+8', '+5', '-6']) == 5)
    assert(process_data2(['+7', '+7', '-2', '-7', '-4']) == 14)

if __name__ == "__main__":
    part1_tests()
    part2_tests()
    dat1()