import pytest

from utils import utils
from day_1 import part1, part2, get_data


def test_example_part1():
    list1, list2 = get_data(utils.SRC_EXAMPLE)
    assert part1(list1, list2) == 11

def test_example_part2():
    list1, list2 = get_data(utils.SRC_EXAMPLE)
    assert part2(list1, list2) == 31

def test_input_part1():
    list1, list2 = get_data(utils.SRC_INPUT)
    assert part1(list1, list2) == 1834060

def test_input_part2():
    list1, list2 = get_data(utils.SRC_INPUT)
    assert part2(list1, list2) == 21607792

if __name__ == '__main__':
    pytest.main()