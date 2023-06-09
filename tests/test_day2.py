from dol_hacking.day2.day2 import process_data1, process_data2, get_input_data

def test_part1_examples():

    assert process_data1(["abcdef"]) == 0
    assert process_data1(["bababc"]) == 0
    assert process_data1(["abbcde"]) == 0
    assert process_data1(["abcccd"]) == 0
    assert process_data1(["aabcdd"]) == 0
    assert process_data1(["abcdee"]) == 0
    assert process_data1(["ababab"]) == 0

def test_part2_examples():
    pass

def test_part1_answer():
    with get_input_data() as data:
        assert process_data1(data) == 0

def test_part2_answer():
    with get_input_data() as data:
        assert process_data2(data) == 0