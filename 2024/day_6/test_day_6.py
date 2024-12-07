import pytest

import aoc
from day_6 import get_data, part1, part2


def test_example_part1():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part1(data) == 41

def test_input_part1():
    data = get_data(aoc.SOURCE.INPUT)
    assert part1(data) == 4988

def test_example_part2():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part2(data) == 6

def test_input_part2():
    data = get_data(aoc.SOURCE.INPUT)
    assert part2(data) == 1697

if __name__ == '__main__':
    pytest.main()