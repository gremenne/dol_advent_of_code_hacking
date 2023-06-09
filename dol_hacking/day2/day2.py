import os
from contextlib import contextmanager

@contextmanager
def get_input_data():
    input_file_path =  os.path.join(os.path.dirname(__file__), "input.txt")
    with open(input_file_path, mode='r') as input_file:
        yield input_file

def process_data1(data):
    pass

def process_data2(data):
    pass

def run():
    with get_input_data() as data:
        answer1 = process_data1(data)
        print(f"The answer to part 1 is: {answer1}")

    with get_input_data() as data:
        answer2 = process_data2(data)
        print(f"The answer to part 2 is: {answer2}")

if __name__ == "__main__":
    run()