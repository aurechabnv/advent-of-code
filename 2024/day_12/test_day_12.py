import pytest

import aoc
from day_12 import get_data, part1, part2


def test_example_part1():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part1(data) == 1930

def test_input_part1():
    data = get_data(aoc.SOURCE.INPUT)
    assert part1(data) == 1485656

def test_example_part2():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part2(data) == 1206

def test_input_part2():
    data = get_data(aoc.SOURCE.INPUT)
    assert part2(data) == 899196

if __name__ == '__main__':
    pytest.main()