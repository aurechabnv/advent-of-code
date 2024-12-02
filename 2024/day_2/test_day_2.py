import pytest

import aoc
from day_2 import part1, part2, get_data


def test_example_part1():
    data = get_data(aoc.SRC_EXAMPLE)
    assert part1(data) == 2

def test_example_part2():
    data = get_data(aoc.SRC_EXAMPLE)
    assert part2(data) == 4

def test_input_part1():
    data = get_data(aoc.SRC_INPUT)
    assert part1(data) == 407

def test_input_part2():
    data = get_data(aoc.SRC_INPUT)
    assert part2(data) == 459

if __name__ == '__main__':
    pytest.main()