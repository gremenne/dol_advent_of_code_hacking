from dol_hacking.day2.day2 import process_line1, process_data1, find_close_match, process_data2, get_input_data

def test_part1_examples_line_by_line():

    assert process_line1("abcdef") == (False, False)
    assert process_line1("bababc") == (True, True)
    assert process_line1("abbcde") == (True, False)
    assert process_line1("abcccd") == (False, True)
    assert process_line1("aabcdd") == (True, False)
    assert process_line1("abcdee") == (True, False)
    assert process_line1("ababab") == (False, True)

def test_part1_examples():

    assert process_data1(["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]) == 12

def test_part2_find_close_match():
    assert find_close_match(["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]) == ("fghij", "fguij")

def test_part2_examples():
    assert process_data2(["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]) == "fgij"

def test_part1_answer():
    with get_input_data() as data:
        assert process_data1(data) == 5727

def test_part2_answer():
    with get_input_data() as data:
        assert process_data2(data) == "uwfmdjxyxlbgnrotcfpvswaqh\n"