import pytest

import aoc
from day_16 import get_data, part1, part2


def test_example_part1():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part1(data) == 7036

def test_example2_part1():
    data = get_data(aoc.SOURCE.EXAMPLE, offset=2)
    assert part1(data) == 11048

def test_input_part1():
    data = get_data(aoc.SOURCE.INPUT)
    assert part1(data) == 105496

def test_example_part2():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part2(data) == 45

def test_example2_part2():
    data = get_data(aoc.SOURCE.EXAMPLE, offset=2)
    assert part2(data) == 64

def test_input_part2():
    data = get_data(aoc.SOURCE.INPUT)
    assert part2(data) == 524

if __name__ == '__main__':
    pytest.main()