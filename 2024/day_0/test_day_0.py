import pytest

from utils import utils
from day_0 import part1, part2, get_data


def test_example_part1():
    data = get_data(utils.SRC_EXAMPLE)
    assert part1(data) == True

def test_example_part2():
    data = get_data(utils.SRC_EXAMPLE)
    assert part2(data) == True

def test_input_part1():
    data = get_data(utils.SRC_INPUT)
    assert part1(data) == True

def test_input_part2():
    data = get_data(utils.SRC_INPUT)
    assert part2(data) == True

if __name__ == '__main__':
    pytest.main()