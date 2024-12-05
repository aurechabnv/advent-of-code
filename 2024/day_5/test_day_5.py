import pytest

from aoc import utils
from day_5 import get_data, part1, part2


def test_example_part1():
    data = get_data(utils.SOURCE.EXAMPLE)
    assert part1(*data) == 143

def test_input_part1():
    data = get_data(utils.SOURCE.INPUT)
    assert part1(*data) == 6498

def test_example_part2():
    data = get_data(utils.SOURCE.EXAMPLE)
    assert part2(*data) == 123

def test_input_part2():
    data = get_data(utils.SOURCE.INPUT)
    assert part2(*data) == 5017

if __name__ == '__main__':
    pytest.main()