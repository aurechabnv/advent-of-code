import pytest

import aoc
from day_15 import get_data, part1, part2


def test_example_part1():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part1(data) == 10092

def test_input_part1():
    data = get_data(aoc.SOURCE.INPUT)
    assert part1(data) == 1463512

def test_example_part2():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part2(data) == 9021

def test_input_part2():
    data = get_data(aoc.SOURCE.INPUT)
    assert part2(data) == 1486520

if __name__ == '__main__':
    pytest.main()