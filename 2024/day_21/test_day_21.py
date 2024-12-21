import pytest

import aoc
from day_21 import get_data, part1, part2


def test_example_part1():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part1(data) == 126384

def test_input_part1():
    data = get_data(aoc.SOURCE.INPUT)
    assert part1(data) == 176452

def test_example_part2():
    data = get_data(aoc.SOURCE.EXAMPLE)
    assert part2(data) == 154115708116294

def test_input_part2():
    data = get_data(aoc.SOURCE.INPUT)
    assert part2(data) == 218309335714068

if __name__ == '__main__':
    pytest.main()