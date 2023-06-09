from dol_hacking.day1.day1 import process_data1, process_data2, get_input_data

def test_part1_examples():
    assert process_data1(['+1', '-2', '+3', '+1']) == 3
    assert process_data1(['+1', '+1', '+1']) == 3
    assert process_data1(['+1', '+1', '-2']) == 0
    assert process_data1(['-1', '-2', '-3']) == -6

def test_part2_examples():
    assert process_data2(['+1', '-1']) == 0
    assert process_data2(['+3', '+3', '+4', '-2', '-4']) == 10
    assert process_data2(['-6', '+3', '+8', '+5', '-6']) == 5
    assert process_data2(['+7', '+7', '-2', '-7', '-4']) == 14

def test_part1_answer():
    with get_input_data() as data:
        assert process_data1(data) == 587

def test_part2_answer():
    with get_input_data() as data:
        assert process_data2(data) == 83130